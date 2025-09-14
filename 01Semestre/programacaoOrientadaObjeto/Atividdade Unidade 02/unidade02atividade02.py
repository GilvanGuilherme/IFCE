# 2) Crie uma classe chamada Livro que tenha um método construtor com os seguintes atributos:
# titulo: o título do livro.
# autor: o nome do autor.
# ano_publicacao: o ano de publicação do livro.
# preco: o preço do livro.
# Crie dois objetos dessa classe, cada um com atributos diferentes, e imprima as informações de cada livro no formato: "Título: {titulo}, Autor: {autor}, Ano: {ano_publicacao}, Preço: R${preco}"


class Livro:
    def __init__(self, titulo, autor, ano_publicacao, preco):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.preco = preco

livro1 = Livro("Codigo LImpo", "Robert Martin", 2009, 25.90)
livro2 = Livro("Algoritmos JavaScript", "Loyane Groner", 2019, 59.90)

print(f"Título: {livro1.titulo}, Autor: {livro1.autor}, Ano: {livro1.ano_publicacao}, Preço: R${livro1.preco}")
print(f"Título: {livro2.titulo}, Autor: {livro2.autor}, Ano: {livro2.ano_publicacao}, Preço: R${livro2.preco}")
