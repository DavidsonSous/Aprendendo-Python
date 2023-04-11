# Faça um algorítmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

produto = float(input('Quanto custa o produto?: R$ '))
desconto = produto - (produto*5/100)
print(' ')
print (f'O produto que você comprou custava R$ {produto:.2f}, porém, demos um desconto de 5% e seu novo preço é de R$ {desconto:.2f}.')