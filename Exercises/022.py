# Crie um programa que leia o nome completo de uma pessoa e mostre: 
# O nome com todas as letras maiúsculas e minúsculas. 
# Quantas letras ao todo (sem considerar espaços). 
# Quantas letras tem o primeiro nome.


nome = input("Digite seu Nome Completo: ")
print(nome.upper())
print(nome.lower())
esp = int(nome.count(' '))
letr = int(len(nome))
num = int(letr - esp)
print('Seu nome completo tem {} letras'.format(num))
nome2 = nome.split()
print('Seu primeiro nome tem {} letras'.format(len(nome2[0])))
