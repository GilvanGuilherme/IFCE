# 2 Escreva um programa que calcule o fatorial de um número inteiro informado pelo usuário.
numero = int(input("Digite o número: "))
fatorial=1
for i in range(numero, 0, -1):
    fatorial = fatorial * i
print(f"O fatorial de {numero} é igual {fatorial}")