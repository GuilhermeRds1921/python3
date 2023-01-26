# Desenvolva um programa que leia o comprimento de
# três retas e diga ao usuário se elas podem 
# ou não formar um trângulo.

a = float(input("Digite a Primeira Reta: "))
b = float(input("Digite a Segunda Reta: "))
c = float(input("Digite a Terceira Reta: "))
if a < b:
    ax = a
    a = c
    c = ax
if b < c:
    ax = b
    b = c
    c = ax
if a < b:
    ax = a
    a = c
    c = ax
if a < b + c:
    print("Pode formar um Triângulo ")
else:
    print("Não pode formar um Triângulo ")