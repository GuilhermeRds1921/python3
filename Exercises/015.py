# Escreva um programa que pergunte a quantidade de Km
# percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro
# custa R$60 por dia e R$0.15 por Km rodado.

km = float(input("Quantos km percorreu?: "))
dia = int(input("Quantos dias ele foi alugado?: "))
print("O valor a ser pago é: R${:.2f}".format(km * 0.15 + dia * 60))