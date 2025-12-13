set -e

docker run -d --platform linux/amd64 -p 9000:8080 --name devops_challenge devops-challenge:test

curl "http://localhost:9000/2015-03-31/functions/function/invocations" -d \
  '{"input": "tabela-fipe-historico-precos.csv", "output": "preco_medio_por_ano_marca.json"}'

docker rm devops_challenge