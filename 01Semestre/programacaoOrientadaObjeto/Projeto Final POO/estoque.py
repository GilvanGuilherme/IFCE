from produto import Produto
import arquivo

class Estoque:
    def __init__(self):
        self.produtos = arquivo.carregar_produtos()

    def adicionar_produto(self, produto):
        self.produtos.append(produto)
        arquivo.salvar_produtos(self.produtos)

    def listar_produtos(self):
        for p in self.produtos:
            print(p)

    def remover_produto(self, nome_produto):
        self.produtos = [p for p in self.produtos if p.nome != nome_produto]
        arquivo.salvar_produtos(self.produtos)

    def adicionar_quantidade(self, nome_produto, quantidade):
        for p in self.produtos:
            if p.nome == nome_produto:
                p.adicionar_estoque(quantidade)
        arquivo.salvar_produtos(self.produtos)

    def remover_quantidade(self, nome_produto, quantidade):
        for p in self.produtos:
            if p.nome == nome_produto:
                p.remover_estoque(quantidade)
        arquivo.salvar_produtos(self.produtos)
