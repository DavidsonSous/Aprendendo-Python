# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por Km rodados.

km_rodado = float(input('Quantos kms foram percorridos no total?: '))
dias = int(input('Por quantos dias você alugou o carro?: '))
valor_total = (dias*60.00) + (km_rodado*0.15)
print (' ')
print (f'Você alugou o carro por {dias} dias e percorreu {km_rodado:.2f} km com ele, o valor total a ser pago na agência ao devolver o carro será de R$ {valor_total:.2f}')
 