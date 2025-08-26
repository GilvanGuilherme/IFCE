# 4 Escreva um programa que leia uma sequência de números inteiros informados pelo usuário e imprima os números ímpares dessa sequência.


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
        
    impar = [ i for i in lista if i % 2 == 1 ]
    
# impar = []
# for i in (lista):
#     if i % 2 == 1:
#         impar.append(i)
        
        
  

print(f"Lista final: {lista}")
print(f"Essa é a lista contendo os numeros impares.{impar}")
