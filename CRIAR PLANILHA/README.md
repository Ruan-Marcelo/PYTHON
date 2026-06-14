# Gerador de Planilha de Gestao Financeira Pessoal

Este projeto contem um script Python que cria automaticamente uma planilha Excel para controle financeiro pessoal.

Ao executar o arquivo `app.py`, o programa gera o arquivo `Gestao_Financeira_Pessoal.xlsx` na mesma pasta do script.

## O que o script faz

O script cria uma planilha completa com:

- Dashboard financeiro.
- Controle de lancamentos.
- Gastos fixos.
- Gastos variaveis.
- Ganhos fixos.
- Ganhos variaveis.
- Dinheiro guardado.
- Listas de categorias para validacao de dados.
- Tabelas formatadas.
- Formulas automaticas.
- Graficos de entradas, saidas e valores guardados.
- Resumo mensal.
- Saidas por categoria.

## Estrutura da planilha

A planilha gerada possui as seguintes abas:

- `Dashboard`: resumo visual com indicadores, graficos e filtros por ano e mes.
- `Lancamentos`: registro principal de entradas e saidas financeiras.
- `Gastos Fixos`: controle de despesas recorrentes.
- `Gastos Variaveis`: controle de despesas que mudam a cada mes.
- `Ganhos Fixos`: controle de receitas recorrentes.
- `Ganhos Variaveis`: controle de receitas eventuais.
- `Dinheiro Guardado`: acompanhamento de reservas, investimentos e metas.
- `Categorias`: aba oculta usada para listas e validacoes.

## Requisitos

Antes de executar o projeto, instale o Python e a biblioteca `openpyxl`.

```bash
pip install openpyxl
```

## Como executar

No terminal, entre na pasta do projeto:

```bash
cd "CRIAR PLANILHA"
```

Depois execute:

```bash
python app.py
```

Ao final, sera exibida uma mensagem parecida com:

```text
Planilha criada em: caminho/para/Gestao_Financeira_Pessoal.xlsx
```

## Arquivo gerado

O arquivo criado sera:

```text
Gestao_Financeira_Pessoal.xlsx
```

Ele pode ser aberto no Microsoft Excel, LibreOffice Calc ou outro editor compativel com arquivos `.xlsx`.

## Observacoes

- O ano inicial usado no dashboard e `2026`.
- O mes inicial selecionado no dashboard e `Janeiro`.
- Os valores de exemplo comecam zerados para que voce possa preencher com seus proprios dados.
- A aba `Categorias` fica oculta porque serve apenas como apoio para os menus suspensos da planilha.
