"""
Sistema simples de Controle de Producao Industrial.

O programa usa uma lista para armazenar os produtos e um dicionario
para representar cada produto cadastrado.
"""


produtos = []


def ler_inteiro(mensagem):
    """Le um numero inteiro e repete ate o usuario digitar corretamente."""
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Valor invalido. Digite um numero inteiro.")


def ler_float(mensagem):
    """Le um numero decimal e aceita virgula ou ponto."""
    while True:
        try:
            valor = input(mensagem).replace(",", ".")
            return float(valor)
        except ValueError:
            print("Valor invalido. Digite um numero decimal.")


def buscar_por_codigo(codigo):
    """Procura um produto pelo codigo informado."""
    for produto in produtos:
        if produto["codigo"] == codigo:
            return produto
    return None


def cadastrar_produto():
    """Cadastra um novo produto na lista de produtos."""
    print("\n--- Cadastro de Produto ---")

    codigo = ler_inteiro("Codigo do produto: ")

    if buscar_por_codigo(codigo) is not None:
        print("Ja existe um produto com esse codigo.")
        return

    nome = input("Nome do produto: ").strip()
    setor = input("Setor de fabricacao: ").strip()
    quantidade = ler_inteiro("Quantidade em estoque: ")
    custo = ler_float("Custo unitario: R$ ")

    produto = {
        "codigo": codigo,
        "nome": nome,
        "setor": setor,
        "quantidade": quantidade,
        "custo": custo,
    }

    produtos.append(produto)
    print("Produto cadastrado com sucesso.")


def listar_produtos():
    """Mostra todos os produtos cadastrados."""
    print("\n--- Lista de Produtos ---")

    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
        return

    for produto in produtos:
        print(
            f"Codigo: {produto['codigo']} | "
            f"Nome: {produto['nome']} | "
            f"Setor: {produto['setor']} | "
            f"Estoque: {produto['quantidade']} | "
            f"Custo: R$ {produto['custo']:.2f}"
        )


def buscar_produto():
    """Busca um produto pelo codigo ou por parte do nome."""
    print("\n--- Buscar Produto ---")
    termo = input("Digite o codigo ou nome do produto: ").strip()

    encontrados = []

    for produto in produtos:
        if termo.isdigit() and produto["codigo"] == int(termo):
            encontrados.append(produto)
        elif termo.lower() in produto["nome"].lower():
            encontrados.append(produto)

    if len(encontrados) == 0:
        print("Produto nao encontrado.")
        return

    for produto in encontrados:
        print(
            f"Codigo: {produto['codigo']} | "
            f"Nome: {produto['nome']} | "
            f"Setor: {produto['setor']} | "
            f"Estoque: {produto['quantidade']} | "
            f"Custo: R$ {produto['custo']:.2f}"
        )


def registrar_producao():
    """Registra entrada ou saida de produtos no estoque."""
    print("\n--- Registrar Producao ---")
    codigo = ler_inteiro("Codigo do produto: ")
    produto = buscar_por_codigo(codigo)

    try:
        if produto is None:
            raise LookupError("Codigo de produto inexistente.")

        print("1 - Entrada de itens produzidos")
        print("2 - Saida de itens do estoque")
        opcao = input("Escolha uma opcao: ").strip()

        quantidade = ler_inteiro("Quantidade: ")

        if quantidade <= 0:
            print("A quantidade deve ser maior que zero.")
            return

        if opcao == "1":
            produto["quantidade"] += quantidade
            print("Entrada registrada com sucesso.")
        elif opcao == "2":
            if quantidade > produto["quantidade"]:
                raise ValueError("Nao ha itens suficientes em estoque.")
            produto["quantidade"] -= quantidade
            print("Saida registrada com sucesso.")
        else:
            print("Opcao invalida.")

    except LookupError as erro:
        print(erro)
    except ValueError as erro:
        print(erro)


def consultar_estoque():
    """Mostra o estoque atual e o valor total de cada produto."""
    print("\n--- Estoque Atual ---")

    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
        return

    valor_geral = 0

    for produto in produtos:
        valor_total = produto["quantidade"] * produto["custo"]
        valor_geral += valor_total

        print(
            f"{produto['nome']} - "
            f"Quantidade: {produto['quantidade']} - "
            f"Valor em estoque: R$ {valor_total:.2f}"
        )

    print(f"Valor total geral do estoque: R$ {valor_geral:.2f}")


def mostrar_menu():
    """Exibe o menu principal do sistema."""
    print("\n===== Controle de Producao Industrial =====")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Buscar produto pelo codigo ou nome")
    print("4 - Registrar producao")
    print("5 - Consultar estoque atual")
    print("6 - Encerrar o programa")


def main():
    """Mantem o sistema em execucao ate o usuario escolher sair."""
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opcao: ").strip()

        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            buscar_produto()
        elif opcao == "4":
            registrar_producao()
        elif opcao == "5":
            consultar_estoque()
        elif opcao == "6":
            print("Programa encerrado. Ate mais!")
            break
        else:
            print("Opcao invalida. Tente novamente.")


if __name__ == "__main__":
    main()
