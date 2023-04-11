# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la. Sabendo que cada litro de tinta, pinta uma area de 2m²

largura = float(input('Digite a largura da parede que quer pintar: '))
altura = float(input('Digite a altura da parede que quer pintar: '))
area_total = largura*altura
tinta = area_total/2
print (' ')
print (f'Sua parede tem a dimensão de {largura} x {altura}, sendo assim, sua área total é de {area_total} m². \nPara pintar toda a parede, você vai precisar de {tinta} litros de tinta')
