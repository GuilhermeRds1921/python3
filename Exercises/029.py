# Escreva um programa que leia a velocidade de um carro. 
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi muldato. 
# A multa vai custar R$7,00 para cada Km acima do limite.

vel = float(input("Digite a velocidade do carro: "))
if vel <= 80:
    print("Você está dentro do limite ")
else:
    print("Você está acima do limite ")
    vel = vel - 80
    print("Terá que pagar R${:.2f} de multa ".format(vel * 7))
