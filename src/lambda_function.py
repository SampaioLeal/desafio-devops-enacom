import os
import json
import logging
from typing import Any, Dict
from processa_preco_medio import calcular_medias_por_ano_e_marca
from setup_directories import LOCAL_INPUT_DIR, LOCAL_OUTPUT_DIR, setup_directories

import boto3
from types_boto3_s3.client import S3Client
from botocore.exceptions import ClientError


# Inicializa o cliente fora do handler para aproveitar o reuso de conexão (Warm Start)
s3_client: S3Client = boto3.client('s3')  # type: ignore

logger = logging.getLogger()
logger.setLevel("INFO")


def get_input_from_s3(bucket: str, key: str):
    """
    Baixa o arquivo do S3 para a pasta local.
    Retorna o caminho completo do arquivo baixado.
    """
    local_path = os.path.join(LOCAL_INPUT_DIR, key)

    try:
        logger.info(
            f"Baixando s3://{bucket}/inputs/{key} para {local_path}...")
        s3_client.download_file(
            Bucket=bucket,
            Key=f"inputs/{key}",
            Filename=local_path
        )

        return local_path
    except ClientError as e:
        logger.error(f"Erro ao baixar arquivo {key} do bucket {bucket}: {e}")
        raise e


def upload_output_to_s3(bucket: str, key: str):
    """
    Faz o upload do arquivo JSON local para a pasta 'outputs/' no bucket S3.
    """
    local_path = os.path.join(LOCAL_OUTPUT_DIR, key)

    try:
        logger.info(
            f"Enviando {local_path} para s3://{bucket}/outputs/{key}...")
        s3_client.upload_file(
            Bucket=bucket,
            Filename=local_path,
            Key=f"outputs/{key}",
            ExtraArgs={'ContentType': 'application/json'}
        )
        logger.info(
            f"Arquivo salvo com sucesso em s3://{bucket}/outputs/{key}")
    except ClientError as e:
        logger.error(f"Erro ao salvar arquivo {key} no bucket {bucket}: {e}")
        raise e


def handler(event: Dict[str, Any], context: Any) -> dict[str, Any]:
    try:
        setup_directories()

        input_key = event.get("input")
        output_key = event.get("output")
        bucket_name = os.environ.get("S3_BUCKET")

        if not input_key or not output_key:
            raise ValueError("O evento deve conter chaves 'input' e 'output'.")
        if not bucket_name:
            raise ValueError("Variável de ambiente S3_BUCKET não definida.")

        logger.info(
            f"Iniciando processamento. Input: {input_key} | Output: {output_key}"
        )

        local_input_path = get_input_from_s3(bucket_name, input_key)
        medias = calcular_medias_por_ano_e_marca(local_input_path)
        local_output_path = os.path.join(LOCAL_OUTPUT_DIR, output_key)

        with open(local_output_path, "w", encoding="utf-8") as f:
            json.dump(medias, f, ensure_ascii=False, indent=2)

        logger.info(f"Arquivo JSON gerado localmente em: {local_output_path}")

        upload_output_to_s3(bucket_name, output_key)

        return {
            "statusCode": 200,
            "message": f"Processamento concluído. Arquivo gerado: {local_output_path}"
        }
    except Exception as e:
        logger.error(f"Erro fatal na execução da Lambda: {str(e)}")
        raise e
