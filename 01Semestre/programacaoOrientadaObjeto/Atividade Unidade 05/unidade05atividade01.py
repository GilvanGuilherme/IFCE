
from abc import ABC, abstractmethod

class CartaoWeb(ABC):  
    def __init__(self, destinatario: str):
        self.destinatario = destinatario

    @abstractmethod
    def showMessage(self):
        pass 


class DiaDosNamorados(CartaoWeb):
    def __init__(self, destinatario: str):
        super().__init__(destinatario)  

    def showMessage(self):
        print(f"Feliz Dia dos Namorados, {self.destinatario}! ")


class Natal(CartaoWeb):
    def __init__(self, destinatario: str):
        super().__init__(destinatario)

    def showMessage(self):
        print(f"Feliz Natal, {self.destinatario}!  Ho Ho Ho!")


class Aniversario(CartaoWeb):
    def __init__(self, destinatario: str):
        super().__init__(destinatario)

    def showMessage(self):
        print(f"Feliz Aniversário, {self.destinatario}! Muitas felicidades!")


if __name__ == "__main__":
    cartao: CartaoWeb

  
    cartao = DiaDosNamorados("Maria")
    cartao.showMessage()  

    cartao = Natal("João")
    cartao.showMessage() 

    cartao = Aniversario("Pedro")
    cartao.showMessage()  


# O polimorfismo ocorre quando a variável "cartao", que é do tipo CartaoWeb,
# pode receber objetos de diferentes subclasses (DiaDosNamorados, Natal, Aniversario).
# Mesmo sendo a "mesma variável", o método showMessage() executa de maneira diferente,
# dependendo de qual objeto foi atribuído a ela.
# Isso é polimorfismo: "uma mesma referência" pode se comportar de várias formas,
# de acordo com o objeto que está nela no momento.
# ------------------------------------------------
