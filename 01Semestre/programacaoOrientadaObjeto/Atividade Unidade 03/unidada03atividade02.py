class Restaurante:
    def __init__(self, nomeRestaurante, tipoCozinha):
        self.nomeRestaurante = nomeRestaurante
        self.tipoCozinha = tipoCozinha

    def descreverRestaurante(self):
        print(f"Restaurante: {self.nomeRestaurante} | Tipo de cozinha: {self.tipoCozinha}")

    def abrirRestaurante(self):
        print(f"O restaurante {self.nomeRestaurante} está aberto!")

    def __str__(self):
        return f"Restaurante: {self.nomeRestaurante} | Tipo de cozinha: {self.tipoCozinha}"


if __name__ == "__main__":
    r1 = Restaurante("Sabor Nordestino", "Comida nordestina")
    r2 = Restaurante("La Bella Italia", "Culinária italiana")
    r3 = Restaurante("Sushi House", "Comida japonesa")

    r1.descreverRestaurante()
    r2.descreverRestaurante()
    r3.descreverRestaurante()

    print("\nUsando __str__:")
    print(r1)
    print(r2)
    print(r3)

    print()
    r1.abrirRestaurante()
