

# 01 Questão 

numero01 = int(input("Digite o primeiro número: " ))
numero02 = int(input("Digite o segundo número: " ))
soma = numero01 + numero02
diferenca = numero01 - numero02
produto = numero01*numero02
divisao= numero01/numero02
print(produto)


# 02 Questão 

base = int(input("Digite o valor da base em centimetros: " ))
altura = int(input("Digite o valor da altura em centimetros: " ))

area_Triangulo= (base*altura) / 2
print(f'A area do triângulo é : {area_Triangulo} centimetros quadrados. ')





# 03 Questão 


valor_hora = int(input("Quanto voce ganha por hora trabalhada ? : " ))
horas_dia = int(input("Quantas horas voce trabalha por dia? : " ))
dias_trabalhado = int(input("Quantos dias voce trabalhou este mes: ? "))
salario_dia = valor_hora * horas_dia
salario_mes = salario_dia * dias_trabalhado
print(f'Esse mês você trabalhou {dias_trabalhado} dias e vai ganhar R${salario_mes}.')




# 04 Questão 


idade = int(input('Quantos anos voce tem: ?'))
dias_vivido = idade * 365
print(f'Você viveu um total de {dias_vivido} dias. ')


# 05 Questão

nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')

nome_completo = nome + ' ' + sobrenome
print(f'Seu nome completo é {nome_completo}, seja bem-vindo!')
 
# 06 Questão 

temperatura_fahrenheit = float(input('Digite a temperatura em Fahrenheit: '))

temperatura_celsius = (temperatura_fahrenheit - 32) * 5/9
temperatura_kelvin = temperatura_celsius + 273.15

print(f'{temperatura_fahrenheit}F é igual a {temperatura_celsius}C')
print(f'{temperatura_fahrenheit}F é igual a {temperatura_kelvin}K')


# 07 Questão 


palavra = input('Digite uma palavra: ')

contador= palavra.count('a')

print(f'A letra "a" aparece {contador} vezes na palavra {palavra}.')


# 08 Questão 

palavra = input('Digite uma palavra: ')

palavra_invertida = palavra[::-1]

print(f'A palavra invertida é: {palavra_invertida}')


# 09 Questão 


frase_separada = input('Digite uma frase : ')

frase_junta = frase_separada.replace(' ', '')

print(f'A frase sem espaços é: {frase_junta}')



# 10 Questão

frase = input('Digite a primeira frase: ')

frase_invertida = frase[::-1]
frase_final = frase_invertida.replace('a', '*')


print(f'Aqui vai sua frase modificada: {frase_final}')