## Desafio ENACOM — Processamento de Preço Médio por Ano e Marca

Este projeto processa o arquivo `tabela-fipe-historico-precos.csv` e gera um JSON com o preço médio dos veículos agrupado por `anoModelo` e por `marca`.

### Arquivos
- `tabela-fipe-historico-precos.csv`: arquivo de entrada (colunas: `codigoFipe`, `marca`, `modelo`, `anoModelo`, `mesReferencia`, `anoReferencia`, `valor`).
- `processa_preco_medio.py`: script que processa o CSV e gera o JSON.
- `preco_medio_por_ano_marca.json`: arquivo de saída gerado.

### Requisitos
- Python 3.8+ (recomendado Python 3.10+)

Opcional (ambiente virtual):
```bash
python3 -m venv .venv
source .venv/bin/activate  # macOS/Linux
# No Windows (PowerShell): .venv\\Scripts\\Activate.ps1
```

### Como executar (padrão)
No diretório do projeto:
```bash
python3 processa_preco_medio.py
```
Isso irá ler `tabela-fipe-historico-precos.csv` no diretório atual e gerar `preco_medio_por_ano_marca.json`.

### Opções de linha de comando
Você pode especificar caminhos de entrada/saída:
```bash
python3 processa_preco_medio.py \
  --input tabela-fipe-historico-precos.csv \
  --output preco_medio_por_ano_marca.json
```
Atalhos equivalentes:
```bash
python3 processa_preco_medio.py -i tabela-fipe-historico-precos.csv -o preco_medio_por_ano_marca.json
```

### Formato do JSON gerado
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
- O processamento é feito em streaming (linha a linha), adequado para arquivos grandes.
- Linhas com dados inválidos são ignoradas de forma silenciosa.

### Erros comuns
- "CSV sem cabeçalho ou vazio": confirme que o arquivo possui a primeira linha com nomes de colunas.
- "Cabeçalho inesperado": confirme que existem as colunas `anoModelo`, `marca` e `valor`.

### Ajustes
Se preferir o resultado como uma lista de objetos (por exemplo, `[{"anoModelo": 1992, "marca": "Acura", "precoMedio": 12104.23}]`), adapte e peça para atualizarmos o script.