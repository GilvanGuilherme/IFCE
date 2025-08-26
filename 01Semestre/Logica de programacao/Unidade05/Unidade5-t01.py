# 1 Escreva um programa que imprima a tabuada (Multiplicação) de um número inteiro informado pelo usuário. Imprima a tabuada de maneira organizada.

multiplicando = int(input("Digite um Número: "))

for multiplicador in range (1, 11):
   produto = multiplicando * multiplicador
   
   print(f"{multiplicando}*{multiplicador} é igual {produto}")

   





