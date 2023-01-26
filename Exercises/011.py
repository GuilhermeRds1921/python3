# Faça um programa que leia a largura e a altura de uma parede em
# metros, calcule a sua área e a quantidade de tinta necessária para
# pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

alt = float(input("Digite a Altura da Parede em Metros: "))
larg = float(input("Digite a Largura da Parede em Metros: "))
area = float(alt * larg)
print("Sera nescessário {} Litros de Tinta".format(area / 2))