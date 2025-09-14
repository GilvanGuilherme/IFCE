# 1) Crie uma classe chamada Carro. A classe deve ter um método construtor que inicializa os seguintes atributos:
# marca: a marca do carro.
# modelo: o modelo do carro.
# ano: o ano de fabricação do carro.
# cor: a cor do carro.
# Crie dois objetos dessa classe, cada um com atributos diferentes, e imprima as informações dos carros.
class Carro:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca          
        self.modelo = modelo        
        self.ano = ano              
        self.cor = cor              

    def mostrar_informacoes(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}, Cor: {self.cor}")


carro1 = Carro("Toyota", "Corolla", 2020, "Prata")
carro2 = Carro("Honda", "Civic", 2022, "Preto")

carro1.mostrar_informacoes()
