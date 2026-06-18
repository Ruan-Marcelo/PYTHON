# Comparacao entre os paradigmas imperativo e declarativo

O paradigma imperativo e uma forma de programar em que o desenvolvedor escreve o passo a passo que o computador deve seguir. Ou seja, o codigo mostra como uma tarefa deve ser feita.

No sistema de controle de producao, por exemplo, usamos esse estilo quando criamos um menu com `while`, verificamos opcoes com `if`, `elif` e `else`, percorremos a lista de produtos com `for` e alteramos diretamente a quantidade em estoque.

Exemplo de ideia imperativa:

```python
for produto in produtos:
    if produto["codigo"] == codigo:
        produto["quantidade"] += quantidade
```

Nesse caso, o programa mostra claramente cada etapa: percorre a lista, compara o codigo e depois altera a quantidade.

O paradigma declarativo funciona de outro jeito. Nele, o programador se preocupa mais em dizer o que deseja obter, sem detalhar tanto o passo a passo. Esse estilo aparece bastante em linguagens de consulta, como SQL, e tambem em algumas funcoes prontas de Python.

Exemplo de ideia declarativa:

```sql
SELECT * FROM produtos WHERE codigo = 10;
```

Nesse exemplo, a pessoa apenas informa que deseja buscar o produto de codigo 10. O banco de dados decide internamente como fazer essa busca.

Comparando os dois, o paradigma imperativo costuma ser mais facil para iniciantes porque deixa o fluxo do programa bem visivel. Ja o paradigma declarativo pode deixar o codigo mais curto e direto, principalmente em buscas, filtros e consultas.

Neste projeto, o paradigma mais usado foi o imperativo, porque o sistema trabalha com menu, validacoes, cadastro, alteracao de estoque e repeticoes. Isso ajuda a entender melhor a logica do programa e combina bem com o objetivo do exercicio.
