# Infrastructure as Code

A infraestrutura desenvolvida para executar a aplicação de forma eficiente, escalável e com baixo custo consiste em:

- 1 S3 Bucket por ambiente
- 1 módulo da aplicação por ambiente
  - Repositório ECR com tags mutáveis
  - Função Lambda que utiliza a imagem docker de tag `latest`
  - Permissões mínimas para a Lambda apenas ser capaz de executar seu trabalho

## Lambda

O serviço AWS Lambda foi escolhido para ser o motor da aplicação por conta da baixa complexidade da aplicação e baixo uso de recursos do workload, fazendo com que a execução seja mais rápida e barata, mesmo em escala.

Caso a aplicação venha a ter alta utilização de forma frequente recomendo ao time de desenvolvimento a implementação de paralelismo e streaming no processo de leitura do CSV para mantermos a configuração mínima de memória RAM da função Lambda.

## Deploy

Para realizar o deploy basta seguir os passos a seguir:

```sh
terraform init
terraform apply # Erro de criação da lambda é esperado pois ainda não há a imagem docker criada no repositório
```

Na pasta raíz executar os seguintes comandos:

```sh
docker build --platform linux/amd64 --provenance=false -t "$ECR_REGISTRY/$ECR_REPOSITORY:latest" .
docker push "$ECR_REGISTRY/$ECR_REPOSITORY:latest"
```