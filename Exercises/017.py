# Faça um programa que leia o comprimento do
# cateto oposto e do cateto adjacente de um
# Triângulo retângulo, calcue e mostre o
# comprimento da hipotenusa.

from math import sqrt, pow
ca = float(input("Informe o Cateto Adjacente: "))
co = float(input("Informe o Cateto Oposto: "))
hip = float(pow(ca,2) + pow(co,2))
print("A Hipotenusa é {:.2f}".format(sqrt(hip)))