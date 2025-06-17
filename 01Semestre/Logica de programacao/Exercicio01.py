# Resolução da lista de exercícios
# Questão 01

nome = "Gilvan"
idade = 30

print(f"Meu nome é {nome} e eu tenho {idade} anos.")

# Questão 02 

a = 5
b = 10

a, b = b, a

print("Valor de a:", a)
print("Valor de b:", b)


# Questão 03

pi = 3.14
raio = 4
area = pi * raio ** 2

print("A área do círculo é:", area)

# Questão 04

numero1 = 10
numero2= 3.14
nome = "Gilvan"

print(type(numero1))
print(type(numero2))
print(type(nome))

# Questão 05

resultado = 10 + 5 * 2 - 8/2
print("Resultado:", resultado)




# Questão 06

celsius = 25
fahrenheit = (celsius * 9/5) + 32

print(f"A temperatura de {celsius}°C em Fahrenheit é {fahrenheit}°F")


# Questãao 07

x = 10
y = 20

if x != y and x > 0 and y > 0:
    print("As variáveis são diferentes e maiores que zero.")
else:
    print("Condição não satisfeita.")


# Questão 08

resultado = (5 > 3) and (2 < 1)
print("Resultado:", resultado)

#Questao 09

altura_str = "1.75"
altura_float = float(altura_str)

print(f"A altura convertida é: {altura_float}")


# Questão 10


turma_de_python = {"Ana", "Renato", "Gilvan", "Paulo"}
turma_de_java = {"Ana", "Paulo", "Daniel", "Eduarda"}

# Alunos que fazem as duas linguagens
ambos = turma_de_python & turma_de_java
print("Alunos que fazem as duas linguagens:", ambos)

# Alunos que fazem só Python
apenas_python = turma_de_python - turma_de_java
print("Alunos que fazem só Python:", apenas_python)

# Todos os alunos (sem repetição)
todos_os_alunos = turma_de_python | turma_de_java
print("Todos os alunos:", todos_os_alunos)
