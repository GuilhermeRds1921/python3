# Faça um programa que leia um ano qualquer 
# e mostre se ele é Bissexto.

ano = int(input("Digite o Ano: "))
if ano % 4 == 0:
    ano = ano
    if ano % 100 != 0:
        print("{} é Bissexto ".format(ano))
    elif ano % 400 == 0:
        print("{} é Bissexto ".format(ano))
    else:
        print("Não é Bissexto ")
else:
    print("Não é Bissexto ")