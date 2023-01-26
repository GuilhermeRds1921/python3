# Faça um programa que leia uma frase pelo teclado e mostre: 
# Quantas vezes aparece a letra "A". 
# Em que posição ela aparece a primira vez. 
# Em que posiçao ela aparece a última vez.

frase = str(input("Digite uma Frase qualquer: "))
frase = frase.lower()
print('Letra A:',frase.count('a'))
print('Primeiro A pos:',frase.find('a'))
print('Último A pos:',frase.rfind('a'))
