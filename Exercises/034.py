# Escreva um programa que pergunte o salário de um funcionário e
# calcule o valor do seu aumento. Para salários superiores a R$1.250,00, 
# calcule um aumento de 10%. 
# Para os inferiores ou iguais, o aumento é de 15%.

sal = float(input("Digite o seu Salário: "))
if sal >= 1250:
    sal = sal + (sal * 0.1)
else:
    sal = sal + (sal * 0.15)
print("Seu novo salário e de R${:.2f}".format(sal))