# 5 Escreva um programa que leia uma sequência de números inteiros informados pelo usuário e imprima a quantidade de números negativos.


lista = []

while True:
    
    entrada = input("Digite um número (ou 'sair'): ")
    
    if entrada.lower() == 'sair':
        break
    
    try:
        numero = int(entrada)
        lista.append(numero)
        print(f"Lista atual: {lista}") 
    except ValueError:
        print("Por favor, digite um número válido!")
    

            
# negativos = [n for n in lista if n < 0] (LIST COMPREENSION)ou no range
    negativos = []
    for i in (lista):
        if i < 0:
            negativos.append(i)
    print(negativos)

# print(f"Lista final: {lista}")
# print(f"Essa é a lista contendo os numeros negativos.{negativos}")