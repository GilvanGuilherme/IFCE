# Escreva uma função que receba uma lista de números e retorne o valor mínimo encontrado.

def encontrar_minimo(lista):
    if not lista:
        return None
    minimo = lista[0]
    for numero in lista:
        if numero < minimo:
            minimo = numero
    return minimo

entrada = input("Digite os números separados por espaço: ")
numeros = [int(num) for num in entrada.split()]

resultado = encontrar_minimo(numeros)

if resultado is not None:
    print(f"O menor número é: {resultado}")
else:
    print("A lista está vazia!")


