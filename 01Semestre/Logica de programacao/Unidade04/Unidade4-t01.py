# 1) Escreva um programa que leia o nome de um dia da semana e verifique se é um dia útil ou um dia de fim de semana. Caso seja um dia útil, imprima "Dia útil". Caso seja um dia de fim de semana, imprima "Fim de semana".

diaDeHoje = input('Que dia é hoje ?: ')
if diaDeHoje.strip().upper() == "sabado" or diaDeHoje.strip().upper() == "domingo":
    print('Hoje é Fim de semana')
else:
    print('Hoje é dia útil')