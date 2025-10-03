from produto import Produto

def exibir_menu(estoque):
    while True:
        print("\n===== Sistema de Gestão de Estoque =====")
        print("1. Cadastrar novo produto")
        print("2. Listar produtos")
        print("3. Adicionar quantidade a um produto")
        print("4. Remover quantidade de um produto")
        print("5. Remover produto")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            preco = float(input("Preço: "))
            quantidade = int(input("Quantidade: "))
            estoque.adicionar_produto(Produto(nome, preco, quantidade))

        elif opcao == "2":
            estoque.listar_produtos()

        elif opcao == "3":
            nome = input("Produto: ")
            quantidade = int(input("Quantidade: "))
            estoque.adicionar_quantidade(nome, quantidade)

        elif opcao == "4":
            nome = input("Produto: ")
            quantidade = int(input("Quantidade: "))
            estoque.remover_quantidade(nome, quantidade)

        elif opcao == "5":
            nome = input("Produto: ")
            estoque.remover_produto(nome)

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida!")
