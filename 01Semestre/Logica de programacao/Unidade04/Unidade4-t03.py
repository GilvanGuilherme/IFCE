# 3) Escreva um programa que receba o salário de uma pessoa e diga quanto ela pagará apenas de Imposto de Renda. Considere as seguintes faixas de incidência do imposto:

# até R$ 2.259,20 – isento;

# de R$ 2.259,21 a R$ 2.826,65 – 7,5%;

# de R$ 2.826,66 a R$ 3.751,05 – 15%

# de R$ 3.751,06 a 4.664,68 – 22,5%; e

# acima de R$ 4.664,68 – 27,5%.

while True:
    salario = float(input("Digite o valor do seu Salário: R$ "))

    if salario < 2259.21:
        taxa = 0
        imposto = (taxa / 100) * salario
        print("Você está isento de imposto de renda esse ano.")

    elif 2259.20 < salario < 2826.66:
        taxa = 7.5
        imposto = (taxa / 100) * salario
        print(f"Seu imposto de renda é de {imposto} Reais")

    elif 2826.65 < salario < 3751.06:
        taxa = 15
        imposto = (taxa / 100) * salario
        print(f"Seu imposto de renda é de {imposto} Reais")

    elif 3751.05 < salario < 4664.68:
        taxa = 22.5
        imposto = (taxa / 100) * salario
        print(f"Seu imposto de renda é de {imposto} Reais")

    elif salario > 4664.67:
        taxa = 27.5
        imposto = (taxa / 100) * salario
        print(f"Seu imposto de renda é de {imposto} Reais")

    sair = input("Deseja sair: s/n ? ")
    if sair.lower() == "s":
        print("Programa Encerrado")
        break