# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

num = int(input("Digite um Número: "))
print("Seu Dobro: {}\nSeu Triplo: {}\nSua Raiz: {}".format(num * 2, num * 3, pow(num, 0.5)))