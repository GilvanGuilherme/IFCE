class Restaurante:
    def __init__(self, nomeRestaurante, tipoCozinha, numeroServidos=0):
        self.nomeRestaurante = nomeRestaurante
        self.tipoCozinha = tipoCozinha
        self.numeroServidos = numeroServidos

    def descreverRestaurante(self):
        print(f"Restaurante: {self.nomeRestaurante} | Tipo de cozinha: {self.tipoCozinha}")

    def abrirRestaurante(self):
        print(f"O restaurante {self.nomeRestaurante} está aberto!")

    def getNumeroServidos(self):
        return self.numeroServidos

    def setNumeroServidos(self, valor):
        self.numeroServidos = valor

    def incrementeNumeroServidos(self, valor):
        atual = self.getNumeroServidos()
        self.setNumeroServidos(atual + valor)


if __name__ == "__main__":
    restaurante = Restaurante("Sabor Nordestino", "Comida típica")

    print(f"Número de clientes atendidos: {restaurante.getNumeroServidos()}")

    restaurante.setNumeroServidos(20)
    print(f"Número atualizado de clientes: {restaurante.getNumeroServidos()}")

    restaurante.incrementeNumeroServidos(15)
    print(f"Número de clientes após incremento: {restaurante.getNumeroServidos()}")
