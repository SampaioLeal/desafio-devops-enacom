#!/bin/bash

handle_error() {
  echo "An error occurred in function $FUNCNAME on line $BASH_LINENO"
  docker stop devops_challenge
  docker rm devops_challenge
  exit 1
}

trap 'handle_error' ERR

echo "Running container..."
docker run -d --platform linux/amd64 -p 9000:8080 --name devops_challenge \
  -e AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID \
  -e AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY \
  -e S3_BUCKET=$S3_BUCKET \
  devops-challenge:test

echo ""
echo "Running test request..."
curl "http://localhost:9000/2015-03-31/functions/function/invocations" -d \
  '{"input": "tabela-fipe-historico-precos.csv", "output": "preco_medio_por_ano_marca.json"}'

echo ""
echo ""
echo "Stopping and removing container..."
docker stop devops_challenge
docker rm devops_challenge