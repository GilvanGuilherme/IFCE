palavras = []
for i in range(3):
    entrada = input("Digite uma palavra:  ")
    if entrada.lower() == 'sair':
        break
    palavras.append(entrada)
print("\nEssa é a lista na ordem inversa:")
print(palavras[::-1])

# ITEM B

for i in range(len(palavras)):
    if palavras[i].lower().startswith("a"):
        palavras[i] = "***"

print("\nEssa é a lista modificada:")
print(palavras)



