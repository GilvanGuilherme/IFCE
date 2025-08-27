# 7 Número de Vogais Peça ao usuário para inserir uma frase. Usando um laço for conte e exiba quantas vogais existem na frase. Lembre de verificar a documentação do módulo String em busca de métodos que facilitem a verificação da letra ser vogal.


while True:
    frase = input("Digite uma frase: ou sair para ENCERRAR!:")
    
    if frase.lower() ==  "sair":
        print ("Programa Encerrado a'te a proxima")
        break 

    vogais = "aeiou"
    contador = 0
    for letra in frase:
        if letra.lower() in vogais:
            contador += 1

    print(f"A frase possui {contador} vogais.")
