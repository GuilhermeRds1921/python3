# Faça um programa que leia três númeors e
# mostre qual é o Maior e qual é o Menor.

num1 = float(input("Digite o Pimeiro Numero: "))
num2 = float(input("Digite o Segundo Numero: "))
num3 = float(input("Digite o Terceiro Numero:"))
if num1 < num3:
    ax = num1
    num1 = num3
    num3 = ax
if num2 < num3:
    ax = num2
    num2 = num3
    num3 = ax
if num1 < num2:
    ax = num1
    num1 = num2
    num2 = ax
print("{} É o Maior ".format(num1))
print("{} É o Meio ".format(num2))
print("{} É o Menor ".format(num3))