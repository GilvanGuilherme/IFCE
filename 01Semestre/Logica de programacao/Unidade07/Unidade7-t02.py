# Escreva uma função que receba uma lista de números e um valor inteiro n, e retorne uma nova lista com os n primeiros valores da lista original.

def primeiros_n_valores(lista, n):
    return lista[:n]

entrada = input("Digite os números separados por espaço: ")
numeros = [int(num) for num in entrada.split()]

n = int(input("Digite quantos valores deseja pegar: "))

nova_lista = primeiros_n_valores(numeros, n)

print(f"Os {n} primeiros valores são: {nova_lista}")
