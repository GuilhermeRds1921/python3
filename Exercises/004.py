# Faça um programa que leia algo pelo teclado e mostre na tela 
# seu tipo primitivo e todas as infomações possíveis sobre ele.

valor = input('Variável: ')
print('O tipo da variável e: ',type(valor))
print('E feito de espacos: ', valor.isspace())
print('E númerico: ', valor.isnumeric())
print('E alfabetico: ', valor.isalpha())
print('E tudo maiúsculo: ', valor.isupper())
print('E tudo minúsculo: ', valor.islower())
print('E capitalizada: ', valor.istitle())
