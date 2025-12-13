import json
import argparse
from processa_preco_medio import calcular_medias_por_ano_e_marca
from setup_directories import setup_directories


def main():
    parser = argparse.ArgumentParser(
        description=(
            "Processa um CSV da tabela FIPE histórica e gera um JSON com o preço "
            "médio por anoModelo e por marca."
        )
    )
    parser.add_argument(
        "--input",
        "-i",
        default="tabela-fipe-historico-precos.csv",
        help="Caminho do arquivo CSV de entrada (padrão: tabela-fipe-historico-precos.csv)",
    )
    parser.add_argument(
        "--output",
        "-o",
        default="preco_medio_por_ano_marca.json",
        help="Caminho do arquivo JSON de saída (padrão: preco_medio_por_ano_marca.json)",
    )

    args = parser.parse_args()

    setup_directories()

    medias = calcular_medias_por_ano_e_marca(f"inputs/{args.input}")

    with open(f"outputs/{args.output}", "w", encoding="utf-8") as f:
        json.dump(medias, f, ensure_ascii=False, indent=2)

    print(f"Arquivo JSON gerado em: {args.output}")


if __name__ == "__main__":
    main()
