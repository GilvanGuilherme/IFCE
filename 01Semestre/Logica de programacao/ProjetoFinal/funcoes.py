def cadastrar_aluno(alunos):
    matricula = input("Matrícula do aluno: ").strip()
    if matricula in alunos:
        print("Aluno já cadastrado!")
        return
    nome = input("Nome do aluno: ").strip()
    alunos[matricula] = {"nome": nome, "disciplinas": set(), "notas": {}}
    print(f"Aluno {nome} cadastrado com matrícula {matricula}.")


def cadastrar_disciplina(disciplinas):
    codigo = input("Código da disciplina: ").strip()
    if codigo in disciplinas:
        print("Disciplina já cadastrada!")
        return
    nome = input("Nome da disciplina: ").strip()
    disciplinas[codigo] = {"nome": nome, "alunos": set()}
    print(f"Disciplina {nome} cadastrada com código {codigo}.")


def matricular_aluno(alunos, disciplinas):
    matricula = input("Matrícula do aluno: ").strip()
    if matricula not in alunos:
        print("Aluno não encontrado!")
        return
    codigo = input("Código da disciplina: ").strip()
    if codigo not in disciplinas:
        print("Disciplina não encontrada!")
        return
    alunos[matricula]["disciplinas"].add(codigo)
    if "notas" not in alunos[matricula]:
        alunos[matricula]["notas"] = {}
    if codigo not in alunos[matricula]["notas"]:
        alunos[matricula]["notas"][codigo] = []
    disciplinas[codigo]["alunos"].add(matricula)
    print(f"Aluno {matricula} matriculado na disciplina {codigo}.")


def lancar_nota(alunos, disciplinas):
    matricula = input("Matrícula do aluno: ").strip()
    if matricula not in alunos:
        print("Aluno não encontrado!")
        return
    codigo = input("Código da disciplina: ").strip()
    if codigo not in disciplinas or matricula not in disciplinas[codigo]["alunos"]:
        print("Aluno não está matriculado nesta disciplina!")
        return
    try:
        nota = float(input("Digite a nota: ").strip())
    except ValueError:
        print("Nota inválida!")
        return
    alunos[matricula]["notas"][codigo].append(nota)
    print(f"Nota {nota} registrada para o aluno {matricula} na disciplina {codigo}.")


def listar_alunos(alunos):
    for matricula, info in alunos.items():
        print(f"{matricula}: {info['nome']}")


def listar_disciplinas(disciplinas):
    for codigo, info in disciplinas.items():
        print(f"{codigo}: {info['nome']}")


def listar_alunos_disciplina(disciplinas, alunos):
    codigo = input("Código da disciplina: ").strip()
    if codigo not in disciplinas:
        print("Disciplina não encontrada!")
        return
    for matricula in disciplinas[codigo]["alunos"]:
        print(f"{matricula}: {alunos[matricula]['nome']}")


def exibir_boletim(alunos, disciplinas):
    matricula = input("Matrícula do aluno: ").strip()
    if matricula not in alunos:
        print("Aluno não encontrado!")
        return
    print(f"Boletim de {alunos[matricula]['nome']}:")
    for cod, notas in alunos[matricula]["notas"].items():
        nome_disc = disciplinas[cod]["nome"]
        media = sum(notas)/len(notas) if notas else 0
        print(f"{cod} - {nome_disc}: Notas={notas}, Média={media:.2f}")


def calcular_media_geral(alunos, matricula):
    if matricula not in alunos:
        print("Aluno não encontrado!")
        return None
    medias = []
    for notas in alunos[matricula]["notas"].values():
        if notas:
            medias.append(sum(notas)/len(notas))
    if not medias:
        print("Aluno não possui notas cadastradas.")
        return None
    return sum(medias)/len(medias)


def aprovado_em_todas(alunos, matricula):
    if matricula not in alunos:
        print("Aluno não encontrado!")
        return None
    for notas in alunos[matricula]["notas"].values():
        if notas:
            media = sum(notas)/len(notas)
            if media < 6.0:
                return False
    return True


def alterar_nome_aluno(alunos):
    matricula = input("Matrícula do aluno: ").strip()
    if matricula not in alunos:
        print("Aluno não encontrado!")
        return
    novo = input("Novo nome: ").strip()
    alunos[matricula]["nome"] = novo
    print("Nome alterado com sucesso.")


def alterar_nome_disciplina(disciplinas):
    codigo = input("Código da disciplina: ").strip()
    if codigo not in disciplinas:
        print("Disciplina não encontrada!")
        return
    novo = input("Novo nome: ").strip()
    disciplinas[codigo]["nome"] = novo
    print("Nome da disciplina alterado com sucesso.")


def excluir_aluno(alunos, disciplinas):
    matricula = input("Matrícula do aluno a excluir: ").strip()
    if matricula not in alunos:
        print("Aluno não encontrado!")
        return
    for cod in alunos[matricula]["disciplinas"]:
        if cod in disciplinas:
            disciplinas[cod]["alunos"].discard(matricula)
    del alunos[matricula]
    print("Aluno excluído.")


def excluir_disciplina(disciplinas, alunos):
    codigo = input("Código da disciplina a excluir: ").strip()
    if codigo not in disciplinas:
        print("Disciplina não encontrada!")
        return
    for m in list(disciplinas[codigo]["alunos"]):
        if m in alunos:
            alunos[m]["disciplinas"].discard(codigo)
            alunos[m]["notas"].pop(codigo, None)
    del disciplinas[codigo]
    print("Disciplina excluída.")
