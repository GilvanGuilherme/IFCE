
frutas = ("banana", "maca", "uva", "laranja", "maca", "melancia", "uva")

entrada = input("Digite o nome de uma fruta: ")


qtd = frutas.count(entrada)

if qtd > 0:
    print(f"A fruta '{entrada}' aparece {qtd} vez(es) na tupla.")
    indice = frutas.index(entrada)
    print(f"A primeira ocorrência está no índice {indice}.")
else:
    print(f"A fruta '{entrada}' não foi encontrada na tupla.")
