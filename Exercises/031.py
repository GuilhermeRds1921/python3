# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem. Cobrando R$0.50 po Km para
# viagens de até 200Km e R$0.45 para viagens mais longas.

dist = float(input("Digite a distancia da viajem em KM: "))
if dist <= 200:
    print("Custara R${:.2f}".format(dist * 0.5))
else:
    print("Custara R${:.2f}".format(dist * 0.45))