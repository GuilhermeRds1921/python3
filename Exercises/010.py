# Crie um programa que leia quanto dinheiro uma pessoa tem na
# carteira e mostre quantos Dólares ela pode comprar.

num = float(input("Digite quantos Reais você tem: "))
print("Você poderia comprar ${:.2} Dollar".format(num / 5))