# 6 Jogo de Adivinhação Crie um jogo onde o programa escolhe um número aleatório entre 1 e 100. O jogador deve tentar adivinhar o número. Obs. Pesquisa como importar e usar o módulo random para gerar o número aleatório em questão.

#    A cada tentativa, o programa deve dizer se o número é maior ou menor que a tentativa.
#    O jogo termina quando o jogador adivinhar o número correto.
   
import random

numero_aleatorio = random.randint(1,100)
print(f"Faça sua aposta e escolha um numero de 1 a 100 {numero_aleatorio}")


while True:
   try:
      entrada= input("Qual seu Palpite: ?")
      palpite = int(entrada)
      
      if palpite == numero_aleatorio:
         print("Asertou mizeravi")
         break
      
      elif palpite < numero_aleatorio:
         print("Seu numero foi baixo")
         
      elif palpite > numero_aleatorio:
         print ("Seu numero foi alto")
   
   
   except ValueError:
      print(" Digite um Numero Válido! ")
   