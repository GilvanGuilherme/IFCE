class Veiculo:
    total_veiculos = 0

    def __init__(self, placa: str, modelo: str, diaria: float):
        self.__placa = placa
        self.__alugado = False

        
        self.modelo = modelo
        self.diaria = diaria


        Veiculo.total_veiculos += 1


    @property
    def placa(self):
        return self.__placa

    @placa.setter
    def placa(self, novo_valor):
        print("A placa não pode ser modificada após o cadastro!")

    def alugar(self):
        if not self.__alugado:
            self.__alugado = True
            print(f"Veículo {self.modelo} ({self.__placa}) foi alugado com sucesso.")
        else:
            print(f"O veículo {self.modelo} ({self.__placa}) já está alugado.")

    def devolver(self):
        if self.__alugado:
            self.__alugado = False
            print(f"Veículo {self.modelo} ({self.__placa}) foi devolvido e está disponível.")
        else:
            print(f"O veículo {self.modelo} ({self.__placa}) não estava alugado.")

    def status(self):
        estado = "Alugado" if self.__alugado else "Disponível"
        print(f"Status do veículo {self.modelo} ({self.__placa}): {estado}")

    @classmethod
    def mostrar_total_veiculos(cls):
        print(f"Total de veículos cadastrados: {cls.total_veiculos}")


    @staticmethod
    def calcular_preco_aluguel(dias: int, diaria: float):
        return dias * diaria


if __name__ == "__main__":
    
    carro1 = Veiculo("ABC-1234", "Fiat Uno", 100.0)
    carro2 = Veiculo("XYZ-5678", "Toyota Corolla", 200.0)

    carro1.alugar()
    carro1.status()

    carro1.devolver()
    carro1.status()

    print("\nPlaca do carro1:", carro1.placa)
    carro1.placa = "NOVO-9999"  

  
    Veiculo.mostrar_total_veiculos()

    dias = 5
    preco = Veiculo.calcular_preco_aluguel(dias, carro2.diaria)
    print(f"\nPreço do aluguel de {dias} dias do {carro2.modelo}: R$ {preco:.2f}")
