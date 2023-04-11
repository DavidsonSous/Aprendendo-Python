# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Considere: US$1.00 = R$ 3,27

valor = float(input('Digite quanto reais você tem na carteira neste momento: R$ '))
conversao = valor/3.27
print (' ') 
print (f'Você informou que tem neste momento na carteira R$ {valor:.2f} e com esse valor, você pode comprar U$ {conversao:.2f}.')
