from abc import ABC, abstractmethod

class MetodoPagamento(ABC):
    def __init__(self, valor: float):
        self.valor = valor

    @abstractmethod
    def pagar(self):
        pass



class CartaoCredito(MetodoPagamento):
    def pagar(self):
        taxa = self.valor * 0.05  
        valor_final = self.valor + taxa
        print(f"[Cartão de Crédito]")
        print(f"Valor original: R$ {self.valor:.2f}")
        print(f"Taxa (5%): R$ {taxa:.2f}")
        print(f"Valor final a pagar: R$ {valor_final:.2f}\n")


class BoletoBancario(MetodoPagamento):
    def pagar(self):
        desconto = self.valor * 0.02  
        valor_final = self.valor - desconto
        print(f"[Boleto Bancário]")
        print(f"Valor original: R$ {self.valor:.2f}")
        print(f"Desconto (2%): R$ {desconto:.2f}")
        print(f"Valor final a pagar: R$ {valor_final:.2f}\n")


class Pix(MetodoPagamento):
    def pagar(self):
        print(f"[PIX]")
        print(f"Valor original: R$ {self.valor:.2f}")
        print(f"Valor final a pagar: R$ {self.valor:.2f} (sem acréscimo ou desconto)\n")



if __name__ == "__main__":
    print("=== Sistema de Pagamentos ===")
    valor = float(input("Digite o valor da compra: R$ "))

    print("\nEscolha o método de pagamento:")
    print("1 - Cartão de Crédito")
    print("2 - Boleto Bancário")
    print("3 - Pix")
    opcao = int(input("Opção: "))

    pagamento: MetodoPagamento

    if opcao == 1:
        pagamento = CartaoCredito(valor)
    elif opcao == 2:
        pagamento = BoletoBancario(valor)
    elif opcao == 3:
        pagamento = Pix(valor)
    else:
        print("Opção inválida!")
        exit()

    pagamento.pagar()



# O polimorfismo facilitou a implementação porque usamos a mesma referência
# "pagamento" (do tipo MetodoPagamento) para lidar com diferentes formas de pagamento.
# Assim, não precisamos criar vários códigos separados para cada tipo.
#
# A vantagem de usar uma interface abstrata é que ela garante que
# todas as formas de pagamento terão obrigatoriamente o método "pagar()".
# Isso deixa o sistema flexível: se no futuro quisermos adicionar outro
# método de pagamento (ex: PayPal, PicPay, Criptomoeda),
# basta criar uma nova classe que herde de MetodoPagamento e implemente o pagar().
# O restante do sistema não precisa ser alterado.
