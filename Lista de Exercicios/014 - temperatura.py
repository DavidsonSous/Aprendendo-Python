# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

celsius = float(input('Digite a temperatura em Graus Celsius: º'))
conversao = ((9*celsius)/5)+32
print (' ')
print (f'A temperatura em graus Celsius é de {celsius} ºC e convertendo para Fahrenheit, equivale a {conversao} ºF.')