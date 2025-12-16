# Desafio ENACOM — Processamento de Preço Médio por Ano e Marca

Este projeto é responsável por processar arquivos CSV oriundos de um Bucket S3 ou da pasta local `src/inputs` e gerar um arquivo JSON com o preço médio dos veículos agrupado por `anoModelo` e por `marca`.

## Dependências

- Terraform ou OpenTofu
- Python 3.8+ (recomendado Python 3.10+)
- AWS CLI

## Executando

### Local

Para executar o projeto na sua máquina recomendamos o uso de [devcontainers](https://containers.dev/) para maior isolamento de dependências.

Primeiro é necessário popular a pasta `src/inputs` com algum CSV contendo o histórico de preços da Tabela Fipe.
Esse primeiro passo pode ser simplificado com o comando abaixo:

```sh 
mkdir src/inputs
cp examples/tabela-fipe-historico-precos.csv src/inputs
```

Após o arquivo estar na pasta correta execute o comando abaixo para executar o projeto:

```sh
cd src
python3 cli.py
```

Isso irá ler por padrão o arquivo `src/inputs/tabela-fipe-historico-precos.csv` e gerar o resultado em `src/outputs/preco_medio_por_ano_marca.json`.

Para especificar um arquivo de entrada e um de saída é necessário usar as respectivas flags no comando de execução:

```sh
cd src
python3 cli.py -i meu-arquivo.csv -o resultado.json
```

O comando acima vai ler o arquivo na pasta `src/inputs` e gerar um arquivo na pasta `src/outputs`.

### Nuvem

O projeto foi adaptado para ser executado na nuvem AWS utilizando o serviço AWS Lambda e AWS S3.
O Lambda Handler é responsável por gerenciar os dados do evento no seguinte formato `{ "input": "", "output": "" }` e executar os seguintes passos:

1. Baixar o arquivo especificado na chave `input` via bucket S3 especificado na variável de ambiente `S3_BUCKET`. Obs: os arquivos sempre serão lidos utilizando o padrão `s3://[BUCKET]/inputs/[ARQUIVO]`
2. Processar o CSV e gerar o arquivo JSON
3. Fazer upload do resultado para o bucket S3 utilizando o padrão `s3://[BUCKET]/outputs/[ARQUIVO]`

- Lambda Handler: `src/lambda_function.py`

## Formato do JSON gerado
Estrutura: `{ "<anoModelo>": { "<marca>": <precoMedio> } }`

Exemplo (parcial):
```json
{
  "1992": {
    "Acura": 12104.23,
    "Audi": 14567.89
  },
  "1995": {
    "Acura": 49296.0
  }
}
```

Notas:
- Médias são arredondadas para 2 casas decimais.
- Linhas com dados inválidos são ignoradas de forma silenciosa.

## Erros comuns
- "CSV sem cabeçalho ou vazio": confirme que o arquivo possui a primeira linha com nomes de colunas.
- "Cabeçalho inesperado": confirme que existem as colunas `anoModelo`, `marca` e `valor`.