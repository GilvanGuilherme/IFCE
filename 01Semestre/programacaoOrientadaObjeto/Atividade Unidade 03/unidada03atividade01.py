from datetime import datetime
import random

class Usuario:
    def __init__(self, rg=0, cpf=0, nome="Não informado", dataNascimento=datetime(1900, 1, 1)):
        self.__rg = rg
        self.__cpf = cpf
        self.__nome = nome
        self.__dataNascimento = dataNascimento

    def set_rg(self, rg):
        self.__rg = rg

    def set_cpf(self, cpf):
        self.__cpf = cpf

    def set_nome(self, nome):
        self.__nome = nome

    def set_dataNascimento(self, dataNascimento):
        self.__dataNascimento = dataNascimento

    def get_rg(self):
        return self.__rg

    def get_cpf(self):
        return self.__cpf

    def get_nome(self):
        return self.__nome

    def get_dataNascimento(self):
        return self.__dataNascimento


class Conta:
    def __init__(self, agencia, usuario, dataAbertura, saldo):
        self.__agencia = agencia
        self.__usuario = usuario
        self.__dataAbertura = dataAbertura
        self.__saldo = saldo

    def get_agencia(self):
        return self.__agencia

    def get_usuario(self):
        return self.__usuario

    def get_dataAbertura(self):
        return self.__dataAbertura

    def get_saldo(self):
        return self.__saldo


if __name__ == "__main__":
    usuario = Usuario()

    rg = int(input("Digite o RG: "))
    cpf = int(input("Digite o CPF: "))
    nome = input("Digite o nome: ")
    dataNascimento = datetime.strptime(input("Digite a data de nascimento (dd/mm/aaaa): "), "%d/%m/%Y")

    usuario.set_rg(rg)
    usuario.set_cpf(cpf)
    usuario.set_nome(nome)
    usuario.set_dataNascimento(dataNascimento)

    agencia = random.randint(0, 999)
    dataAbertura = datetime.now()
    saldo = float(input("Digite o saldo inicial: "))

    conta = Conta(agencia, usuario, dataAbertura, saldo)

    print("\n---- Dados da Conta ----")
    print(f"Agência: {conta.get_agencia()}")
    print(f"Data de abertura: {conta.get_dataAbertura().strftime('%d/%m/%Y %H:%M')}")
    print(f"Saldo: R$ {conta.get_saldo():.2f}")

    print("\n---- Dados do Usuário ----")
    print(f"Nome: {conta.get_usuario().get_nome()}")
    print(f"RG: {conta.get_usuario().get_rg()}")
    print(f"CPF: {conta.get_usuario().get_cpf()}")
    print(f"Data de nascimento: {conta.get_usuario().get_dataNascimento().strftime('%d/%m/%Y')}")
