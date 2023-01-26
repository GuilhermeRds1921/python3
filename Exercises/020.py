# O mesmo professor do desafio anterior quer sortear a ordem de 
# apresentação de trabalhos dos alunos. Faça um programa que leia 
# o nome dos quatro alunos e mostre a ordem sorteada.

import random
n1 = input("Digite Primiero Nome: ")
n2 = input("Digite Segundo Nome: ")
n3 = input("Digite Terceiro Nome: ")
n4 = input("Digite Quarto Nome: ")
lista = [n1,n2,n3,n4]
random.shuffle(lista)
print("A ordem de apresentaçao é: ")
print(lista)
