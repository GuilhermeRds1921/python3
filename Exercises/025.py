# Crie um programa que leia o nome de uma pessoa
# e diga se ela tem "Silva" no nome.

nome = input('Digite seu Nome Completo: ')
nome = nome.upper().split()
print('SILVA' in nome)
