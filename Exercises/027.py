# Faça um programa que leia o nome completo de uma pessoa, 
# mostrando em seguida o primeiro e o último nome separadamente.

nome = input('Digite seu Nome Completo: ')
nome = nome.split()
ult = int(len(nome))
print('Primeiro:',nome[0])
print('Último:',nome[int(ult - 1)])
