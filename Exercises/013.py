# Faça um algoritmo que leia o salário de um funcionãrio e mostre seu
# novo salário, com 15% de aumento.

sal = float(input("Digite o Salário: "))
alm = float(sal + (sal * 0.15))
print("O Salário com um aumento de 15% é: {:.2f}".format(alm))