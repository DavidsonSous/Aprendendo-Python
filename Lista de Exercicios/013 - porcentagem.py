# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite seu salário atual: R$ '))
aumento = salario + (salario*15/100)
print (f'O seu salário era de R$ {salario:.2f}, porém, você recebeu um aumento de 15% e seu novo salário passou a ser R$ {aumento:.2f}')