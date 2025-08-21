# 4) Escreva um programa que peça ao usuário um número entre 1 e 100. O programa deve verificar:

# Se o número é divisível por 3, exiba "Número divisível por 3".

# Se o número é divisível por 5, exiba "Número divisível por 5".

# Se o número é divisível por 3 e 5, exiba "Número divisível por 3 e por 5.".

# Caso contrário, exiba "Número comum".

numero=int(input(" Digite um número 1 a 100 : "))
if numero % 3 == 0 and numero % 5 == 0 : 
    print("O numero é divisivel por 3 e por 5")
elif numero % 3 == 0 : 
    print(f"O numero é divisivel por 3")
elif numero % 5 == 0 : 
    print(f"O numero é divisivel por 5")
else:
    print("O numero não tem divisao exata com 3 e 5")