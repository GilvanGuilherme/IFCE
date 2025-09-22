from datetime import datetime
import random

class Conta:
    def __init__(self, agencia, usuario, dataAbertura, saldo=0):
        self.agencia = agencia
        self.usuario = usuario
        self.dataAbertura = dataAbertura
        self.saldo = saldo

    def consultarSaldo(self):
        print(f"Saldo atual: R$ {self.saldo:.2f}")

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente.")

    def transferir(self, valor, outra_conta):
        if valor <= self.saldo:
            self.saldo -= valor
            outra_conta.saldo += valor
            print(f"Transferência de R$ {valor:.2f} realizada com sucesso.")
        else:
            print("Saldo insuficiente para transferência.")


class ContaPoupanca(Conta):
    def __init__(self, agencia, usuario, dataAbertura, saldo=0, rendimento=0.01):
        super().__init__(agencia, usuario, dataAbertura, saldo)
        self.rendimento = rendimento

    def aplicarRendimento(self):
        ganho = self.saldo * self.rendimento
        self.saldo += ganho
        print(f"Rendimento aplicado: R$ {ganho:.2f}")


class ContaCorrente(Conta):
    def __init__(self, agencia, usuario, dataAbertura, saldo=0, tarifa=10):
        super().__init__(agencia, usuario, dataAbertura, saldo)
        self.tarifa = tarifa

    def cobrarTarifa(self):
        self.saldo -= self.tarifa
        print(f"Tarifa de R$ {self.tarifa:.2f} cobrada.")


class ContaEspecial(ContaCorrente):
    def __init__(self, agencia, usuario, dataAbertura, saldo=0, tarifa=10, limite=500):
        super().__init__(agencia, usuario, dataAbertura, saldo, tarifa)
        self.limite = limite

    def consultarSaldo(self):
        print(f"Saldo: R$ {self.saldo:.2f} | Limite: R$ {self.limite:.2f}")

    def sacar(self, valor):
        if valor <= self.saldo + self.limite:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Saldo + limite insuficiente.")

    def transferir(self, valor, outra_conta):
        if valor <= self.saldo + self.limite:
            self.saldo -= valor
            outra_conta.saldo += valor
            print(f"Transferência de R$ {valor:.2f} realizada com sucesso.")
        else:
            print("Saldo + limite insuficiente para transferência.")


if __name__ == "__main__":
    usuario = "Gilvan"
    agencia = random.randint(100, 999)
    dataAbertura = datetime.now()

    conta1 = ContaPoupanca(agencia, usuario, dataAbertura, saldo=1000)
    conta2 = ContaCorrente(agencia, usuario, dataAbertura, saldo=500)
    conta3 = ContaEspecial(agencia, usuario, dataAbertura, saldo=200, limite=800)

    print("\n--- Conta Poupança ---")
    conta1.consultarSaldo()
    conta1.aplicarRendimento()
    conta1.consultarSaldo()

    print("\n--- Conta Corrente ---")
    conta2.consultarSaldo()
    conta2.cobrarTarifa()
    conta2.consultarSaldo()

    print("\n--- Conta Especial ---")
    conta3.consultarSaldo()
    conta3.sacar(900)  
    conta3.consultarSaldo()
    conta3.transferir(50, conta2)
    conta3.consultarSaldo()
