# 3 Escreva um programa que leia uma sequência de números inteiros informados pelo usuário e imprima os números primos dessa sequência.

lista = []

while True:
    
    entrada = input("Digite um número (ou 'sair'): ")
    
    try:
        numero = int(entrada)
        lista.append(numero)
        print(f"Lista atual: {lista}")
    except ValueError:
        print("Por favor, digite um número válido!")
    
    if entrada.lower() == 'sair':
        break
        
    

print(f"Lista final: {lista}")
