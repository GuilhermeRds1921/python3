# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros
# e milímetros.

num = float(input("Digite a Médida em Metros: "))
cent = float(num * 100)
mili = float(num * 1000)
print("Centimetros: {}\nMilímetros: {}".format(cent, mili))