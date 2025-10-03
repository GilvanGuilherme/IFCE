class Produto:
    def __init__(self, nome, preco, quantidade):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade = quantidade

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, novo_preco):
        if novo_preco >= 0:
            self.__preco = novo_preco

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, nova_quantidade):
        if nova_quantidade >= 0:
            self.__quantidade = nova_quantidade

    def adicionar_estoque(self, quantidade):
        self.__quantidade += quantidade

    def remover_estoque(self, quantidade):
        if quantidade <= self.__quantidade:
            self.__quantidade -= quantidade

    def __str__(self):
        return f"{self.__nome} - R${self.__preco:.2f} - {self.__quantidade} unid."
