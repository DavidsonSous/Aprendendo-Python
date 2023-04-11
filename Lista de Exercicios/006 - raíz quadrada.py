# Crie um algoritmo que leia um número e mostre o seu dobro, seu triplo e a raiz quadrada.

n1 = int(input('Digite um número: '))
dobro = n1*2
triplo = n1*3
raiz_quadrada = n1**(1/2)
print (' ')
print (f'O número que você digitou foi: {n1}. \nO dobro deste número é: {dobro}. \nO triplo deste número é: {triplo}. \nE a raiz quadrada é: {raiz_quadrada:.2f}')