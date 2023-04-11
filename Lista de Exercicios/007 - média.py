# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média.

prova1 = float(input('Digite sua nota na prova 1: '))
prova2 = float(input('Digite sua nota na prova 2: '))
media = (prova1+prova2)/2
print (' ')
print (f'Você tirou {prova1:.1f} pontos na primeira prova e {prova2:.1f} pontos na segunda, sendo assim, a sua média ficou: {media:.1f}.')