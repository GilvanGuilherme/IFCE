def salvar_produtos(produtos):
    with open("produtos.txt", "w") as arquivo:
        for p in produtos:
            arquivo.write(f"{p.nome};{p.preco};{p.quantidade}\n")


def carregar_produtos():
    produtos = []
    try:
        with open("produtos.txt", "r") as arquivo:
            for linha in arquivo:
                nome, preco, quantidade = linha.strip().split(";")
                from produto import Produto
                produtos.append(Produto(nome, float(preco), int(quantidade)))
    except FileNotFoundError:
        pass
    return produtos
