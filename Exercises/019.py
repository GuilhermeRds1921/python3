# Um professor quer sortear um dos seus quatro alunos para apagar 
# o quadro. Faça um programa que ajude ele, lendo o nome deles e 
# escrevendo o nome do escolhido.


import random
alun1 = input("Digite o nome do Primeiro Aluno: ")
alun2 = input("Digite o nome do Segundo Aluno: ")
alun3 = input("Digite o nome do Terceiro Aluno: ")
alun4 = input("Digite o nome do Quarto Aluno: ")
lista = [alun1, alun2, alun3, alun4]
escolhido = random.choice(lista)
print("O aluno escolhido foi {}".format(escolhido))