# Crie uma função chamada analisa_lista que recebe uma lista de números como parâmetro e retorna um dicionário contendo a soma de todos os números, a média dos números e o maior e o menor número da lista.



def analisa_lista(lista):
    if not lista:
        return {
            "soma": 0,
            "media": None,
            "maior": None,
            "menor": None
        }
    
    soma = sum(lista)
    media = soma / len(lista)
    maior = max(lista)
    menor = min(lista)
    
    return {
        "soma": soma,
        "media": media,
        "maior": maior,
        "menor": menor
    }

entrada = input("Digite os números separados por espaço: ")
numeros = [int(num) for num in entrada.split()]

resultado = analisa_lista(numeros)

print(f"Soma: {resultado['soma']}")
print(f"Média: {resultado['media']}")
print(f"Maior número: {resultado['maior']}")
print(f"Menor número: {resultado['menor']}")
