#        Jogo da Adivinhação
# Escreva um programa que faça o computador "pensar" em um 
# número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
# qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
b = randint(0,5)
a = int(input("Escreva um Número de 0 a 5: "))
if a==b:
    print("Você acertou ")
else:
    print("Você errou ")
print("O número era {}".format(b))
