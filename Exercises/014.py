# Escreva um programa que converta uma temperatura
# digitando em ºC e converta para ºF.

temp = float(input("Informe a Temperatura em Cº: "))
f = float((temp * 9 / 5) + 32)
print("A temperatura {}Cº é o que vale {}ºF".format(temp, f))