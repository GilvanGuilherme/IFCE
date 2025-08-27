alunos = {}  
while True:
    print("***Escoha Uma Opção***")
    print("1. Cadastrar aluno")
    print("2. Listar alunos")
    print("0. Sair")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        matricula = input("Digite a matrícula do aluno: ").strip()
        if matricula in alunos:
            print("Já existe um aluno com esta matrícula!")
        else:
            nome = input("Digite o nome do aluno: ").strip()
            alunos[matricula] = {
                "nome": nome,
                "disciplinas": set(),
                "notas": {}
            }
            print("Aluno cadastrado com sucesso!")

    elif opcao == "2":
        if not alunos:
            print(" Nenhum aluno cadastrado ainda.")
        else:
            print("\n Lista de alunos:")
            for matricula, dados in alunos.items():
                print(f"{matricula} - {dados['nome']}")

    elif opcao == "0":
        print(" Saindo do programa...")
        break

    else:
        print("Opção inválida, tente novamente.")
