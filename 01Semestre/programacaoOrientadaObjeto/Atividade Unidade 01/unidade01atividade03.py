# 3. Controle de Tarefas
# Crie um programa que gerencie uma lista de tarefas. Cada tarefa deve ser representada por um dicionário contendo:
# Título da tarefa
# Descrição
# Status (Pendente ou Concluído)
# O programa deve permitir:
# Adicionar uma nova tarefa.
# Marcar uma tarefa como concluída.
# Listar todas as tarefas, separando as concluídas das pendentes.# controle_tarefas.py

tarefas = []

def adicionar_tarefa():
    titulo = input("Título da tarefa: ")
    descricao = input("Descrição da tarefa: ")
    tarefas.append({"titulo": titulo, "descricao": descricao, "status": "Pendente"})
    print("Tarefa adicionada!\n")

def concluir_tarefa():
    titulo = input("Título da tarefa a concluir: ")
    for tarefa in tarefas:
        if tarefa["titulo"] == titulo:
            tarefa["status"] = "Concluída"
            print(f"Tarefa '{titulo}' concluída!\n")
            return
    print("Tarefa não encontrada!\n")

def listar_tarefas():
    print("\n=== Tarefas Pendentes ===")
    for tarefa in tarefas:
        if tarefa["status"] == "Pendente":
            print(f"{tarefa['titulo']}: {tarefa['descricao']}")
    print("\n=== Tarefas Concluídas ===")
    for tarefa in tarefas:
        if tarefa["status"] == "Concluída":
            print(f"{tarefa['titulo']}: {tarefa['descricao']}")
    print()

def menu():
    while True:
        print("1 - Adicionar Tarefa")
        print("2 - Concluir Tarefa")
        print("3 - Listar Tarefas")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_tarefa()
        elif opcao == "2":
            concluir_tarefa()
        elif opcao == "3":
            listar_tarefas()
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida!\n")

menu()
