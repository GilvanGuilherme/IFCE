import funcoes as f

disciplinas = {
    "D01": {"nome": "Lógica de Programação", "alunos": {"20230001"}},
    "D02": {"nome": "Estruturas de Dados", "alunos": set()},
}

alunos = {
    "20230001": {"nome": "Ana Silva", "disciplinas": {"D01"}, "notas": {"D01":[8,7]}},
}

def menu():
    print("""
=== Sistema Acadêmico ===
1 - Cadastrar aluno
2 - Cadastrar disciplina
3 - Matricular aluno
4 - Lançar nota
5 - Listar alunos
6 - Listar disciplinas
7 - Listar alunos da disciplina
8 - Boletim do aluno
9 - Alterar nome do aluno
10 - Alterar nome da disciplina
11 - Excluir aluno
12 - Excluir disciplina
0 - Sair
""")

def main():
    while True:
        menu()
        opc = input("Escolha: ").strip()
        if opc=="1": f.cadastrar_aluno(alunos)
        elif opc=="2": f.cadastrar_disciplina(disciplinas)
        elif opc=="3": f.matricular_aluno(alunos, disciplinas)
        elif opc=="4": f.lancar_nota(alunos, disciplinas)
        elif opc=="5": f.listar_alunos(alunos)
        elif opc=="6": f.listar_disciplinas(disciplinas)
        elif opc=="7": f.listar_alunos_disciplina(disciplinas, alunos)
        elif opc=="8": f.exibir_boletim(alunos, disciplinas)
        elif opc=="9": f.alterar_nome_aluno(alunos)
        elif opc=="10": f.alterar_nome_disciplina(disciplinas)
        elif opc=="11": f.excluir_aluno(alunos, disciplinas)
        elif opc=="12": f.excluir_disciplina(disciplinas, alunos)
        elif opc=="0": break
        else: print("Opção inválida.")
        f.pause()

if __name__=="__main__":
    main()
