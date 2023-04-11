# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira. 
# Ex: Digite um número: 6.127 o número tem a parte inteira 6

from math import trunc
numero = float(input('Digite um número: '))
print (' ')
print (f'O número que você digitou foi {numero} e a parte inteira dele é {trunc(numero)}')