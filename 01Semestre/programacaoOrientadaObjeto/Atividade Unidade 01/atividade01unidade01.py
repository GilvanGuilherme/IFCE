# 1. Estoque de Produtos
# Crie um programa que simule um sistema de gerenciamento de estoque de uma loja. O programa deve permitir:
# Adicionar um novo produto ao estoque (nome e quantidade).
# Remover um produto pelo nome.
# Atualizar a quantidade de um produto existente.
# Exibir todos os produtos no estoque.
# Dica: Utilize um loop para permitir que o usuário faça várias operações até escolher sair.

print("######## Brilhe Car #########")
estoque = {}

def adicionar_carro():
    carro = input("Digite o nome do carro: ")
    quantidade = int(input("Digite a quantidade: "))
    estoque[carro] = quantidade
    print(f"{carro} adicionado com sucesso!\n")

def remover_carro():
    carro = input("Digite o nome do carro para remover: ")
    if carro in estoque:
        del estoque[carro]
        print(f"{carro} removido com sucesso!\n")
    else:
        print("Carro não encontrado!\n")

def atualizar_quantidade():
    carro = input("Digite o nome do carro: ")
    if carro in estoque:
        quantidade = int(input("Digite a nova quantidade: "))
        estoque[carro] = quantidade
        print(f"Quantidade de {carro} atualizada!\n")
    else:
        print("Carro não encontrado!\n")

def exibir_estoque():
    print("\n=== Estoque de Carros ===")
    if estoque:
        for carro, qtd in estoque.items():
            print(f"{carro}: {qtd}")
    else:
        print("Estoque vazio.")
    print()

def menu():
    while True:
        print("1 - Adicionar Carro")
        print("2 - Remover Carro")
        print("3 - Atualizar Quantidade")
        print("4 - Exibir Estoque")
        print("5 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_carro()
        elif opcao == "2":
            remover_carro()
        elif opcao == "3":
            atualizar_quantidade()
        elif opcao == "4":
            exibir_estoque()
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida!\n")

# Inicia o programa
menu()
