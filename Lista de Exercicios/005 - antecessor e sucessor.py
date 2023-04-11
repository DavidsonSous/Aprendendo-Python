# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecesseor.

""" n1 = int(input('Digite um número qualquer: '))
antecessor = n1-1
sucessor = n1+1
print (f'O número digitado foi: {n1}\nO antecessor é: {antecessor}\nO sucessor é: {sucessor}') """

#OU

n = int(input('Digite um número qualquer: '))
print ('O número digitado foi: {}\nO antecessor é: {}\nO sucessor é: {}'.format(n,(n-1),(n+1)))
 