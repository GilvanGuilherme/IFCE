
def cadastrar_aluno(alunos):
    matricula = input("Matrícula: ").strip()
    if matricula == "" or matricula in alunos:
        print("Matrícula inválida ou já existente.")
        return
    nome = input("Nome do aluno: ").strip()
    alunos[matricula] = {"nome": nome, "disciplinas": set(), "notas": {}}
    print(f"Aluno {nome} cadastrado!")

def cadastrar_disciplina(disciplinas):
    codigo = input("Código da disciplina: ").strip().upper()
    if codigo == "" or codigo in disciplinas:
        print("Código inválido ou já existente.")
        return
    nome = input("Nome da disciplina: ").strip()
    disciplinas[codigo] = {"nome": nome, "alunos": set()}
    print(f"Disciplina {nome} cadastrada!")

def matricular_aluno(alunos, disciplinas):
    matricula = input("Matrícula do aluno: ").strip()
    if matricula not in alunos:
        print("Aluno não encontrado.")
        return
    codigo = input("Código da disciplina: ").strip().upper()
    if codigo not in disciplinas:
        print("Disciplina não encontrada.")
        return
    if codigo in alunos[matricula]["disciplinas"]:
        print("Aluno já matriculado.")
        return
    alunos[matricula]["disciplinas"].add(codigo)
    if codigo not in alunos[matricula]["notas"]:
        alunos[matricula]["notas"][codigo] = []
    disciplinas[codigo]["alunos"].add(matricula)
    print(f"Aluno matriculado em {disciplinas[codigo]['nome']}!")

def lancar_nota(alunos, disciplinas):
    matricula = input("Matrícula do aluno: ").strip()
    if matricula not in alunos:
        print("Aluno não encontrado.")
        return
    codigo = input("Código da disciplina: ").strip().upper()
    if codigo not in disciplinas:
        print("Disciplina não encontrada.")
        return
    if codigo not in alunos[matricula]["disciplinas"]:
        print("Aluno não matriculado nesta disciplina.")
        return
    try:
        nota = float(input("Nota (0 a 10): "))
    except:
        print("Valor inválido.")
        return
    if nota < 0 or nota > 10:
        print("Nota fora do intervalo.")
        return
    alunos[matricula]["notas"][codigo].append(nota)
    print("Nota registrada!")

def listar_alunos(alunos):
    print("=== Alunos ===")
    for mat, info in alunos.items():
        print(f"{mat} - {info['nome']} | Disciplinas: {', '.join(info['disciplinas']) if info['disciplinas'] else 'Nenhuma'}")

def listar_disciplinas(disciplinas):
    print("=== Disciplinas ===")
    for cod, info in disciplinas.items():
        print(f"{cod} - {info['nome']} | Alunos matriculados: {len(info['alunos'])}")

def listar_alunos_disciplina(disciplinas, alunos):
    codigo = input("Código da disciplina: ").strip().upper()
    if codigo not in disciplinas:
        print("Disciplina não encontrada.")
        return
    if not disciplinas[codigo]["alunos"]:
        print("Nenhum aluno matriculado.")
        return
    print(f"Alunos em {disciplinas[codigo]['nome']}:")
    for mat in disciplinas[codigo]["alunos"]:
        print(f"- {mat} - {alunos[mat]['nome']}")

def exibir_boletim(alunos, disciplinas):
    matricula = input("Matrícula do aluno: ").strip()
    if matricula not in alunos:
        print("Aluno não encontrado.")
        return
    aluno = alunos[matricula]
    print(f"=== Boletim de {aluno['nome']} ===")
    total_medias = 0
    count_medias = 0
    for cod in aluno["disciplinas"]:
        nome_disc = disciplinas[cod]["nome"]
        notas = aluno["notas"].get(cod, [])
        if notas:
            media = sum(notas)/len(notas)
            status = "Aprovado" if media >= 6 else "Reprovado"
            print(f"{cod} - {nome_disc} | Notas: {notas} | Média: {media:.2f} | {status}")
            total_medias += media
            count_medias += 1
        else:
            print(f"{cod} - {nome_disc} | Sem notas lançadas")
    if count_medias > 0:
        print(f"Média geral: {total_medias/count_medias:.2f}")

def alterar_nome_aluno(alunos):
    matricula = input("Matrícula do aluno: ").strip()
    if matricula in alunos:
        novo = input("Novo nome: ").strip()
        if novo != "":
            alunos[matricula]["nome"] = novo
            print("Nome alterado!")
        else:
            print("Nome inválido.")
    else:
        print("Aluno não encontrado.")

def alterar_nome_disciplina(disciplinas):
    codigo = input("Código da disciplina: ").strip().upper()
    if codigo in disciplinas:
        novo = input("Novo nome: ").strip()
        if novo != "":
            disciplinas[codigo]["nome"] = novo
            print("Nome alterado!")
        else:
            print("Nome inválido.")
    else:
        print("Disciplina não encontrada.")

def excluir_aluno(alunos, disciplinas):
    matricula = input("Matrícula do aluno: ").strip()
    if matricula in alunos:
        for cod in alunos[matricula]["disciplinas"]:
            disciplinas[cod]["alunos"].discard(matricula)
        del alunos[matricula]
        print("Aluno excluído!")
    else:
        print("Aluno não encontrado.")

def excluir_disciplina(disciplinas, alunos):
    codigo = input("Código da disciplina: ").strip().upper()
    if codigo in disciplinas:
        for mat in disciplinas[codigo]["alunos"]:
            alunos[mat]["disciplinas"].discard(codigo)
            alunos[mat]["notas"].pop(codigo, None)
        del disciplinas[codigo]
        print("Disciplina excluída!")
    else:
        print("Disciplina não encontrada.")

def pause():
    input("\nPressione Enter para continuar...")
