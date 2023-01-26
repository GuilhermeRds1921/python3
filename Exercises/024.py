# Crie um programa que leia o nome de uma cidade
# e diga se ela começa ou não com o nome "Santo".

nome = input("Digite o Nome da sua Cidade: ")
nome = nome.split()
print('Santo' in nome[0])
