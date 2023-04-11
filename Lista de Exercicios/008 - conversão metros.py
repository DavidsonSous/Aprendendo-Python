#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metros = float(input('Quantos metros deseja calcular?: '))
centimentros = metros*100
milimetros = metros*1000
print (' ')
print (f'Você deseja transformar {metros} metros em: \nCentímetros: {centimentros:.0f} \nMilimetros: {milimetros:.0f}')
