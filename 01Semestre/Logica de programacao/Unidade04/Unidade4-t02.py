# 2) No mundo de The Witcher, criaturas diferentes apresentam características únicas. Baseado nas pistas abaixo, escreva um programa que identifique o tipo de criatura que Geralt está enfrentando:

apareceDia = input("O monstro aparece de dia? sim/não: ").lower()
apareceNoite = input("O monstro aparece a noite? sim/não: ").lower()
temGarras = input("O monstro tem Garras? sim/não: ").lower()
evitaPrata = input("O monstro evita Prata? sim/não: ").lower()
eRapido = input("O monstro é rapido? sim/não: ").lower()
atacaEmGrupo = input("O monstro ataca em Grupo? sim/não: ").lower()
temOlhos = input("O monstro tem olhos? sim/não: ").lower()
imitaVozHumana = input("O monstro imita a Voz Humana? sim/não: ").lower()
    

if  apareceNoite == "sim" and temGarras == "sim" and evitaPrata =="sim":
    print("O mosntro é um LOBISOMEN. ")

elif eRapido== "sim" and atacaEmGrupo == "sim" and temOlhos == "não" and imitaVozHumana == "não" and evitaPrata == "não":
    print ("O monstro é um NEKKER. ")

elif temOlhos == "sim" and imitaVozHumana == "sim":
    print ("O monstro é um MÍMICO. ")
else:
    print("Criatura desconhecida. Prepare-se para o pior.")