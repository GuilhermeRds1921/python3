# Fça um algoritmo que leia o preço de um produto e mostre seu
# novo preço, com 5% de desconto.

valor = float(input("Digite o Preço de algo: "))
desc = float(valor - (valor * 0.05))
print("O valor com 5% de desconto é: {:.2f}".format(desc))