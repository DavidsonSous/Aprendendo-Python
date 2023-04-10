n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
soma = n1+n2
multiplicacao = n1*n2
divisao = n1/n2
divisao_inteira = n1//n2
exponenciacao = n1**n2
print (' ')
print ('A soma dos números digitados é {}.\nO produto é {}. \nA divisão é {:.3f}.'.format(soma,multiplicacao,divisao), end=' ')
print ('A divisão inteira é {}. \nE a potência é {}.'.format(divisao_inteira,exponenciacao))

#OBSERVAÇÕES

# Quando eu quiser quebrar uma linha: \n

# Quando eu quiser juntar a linha que foi quebrada por dois prints, basta fazer no final da primeira linha Ex: ...divisao), end=' ')

# Quando eu quiser limitar o número de casas decimais, basta usar {:.númerof}




""" print (f'A soma dos números digitados é {soma}, o produto é {multiplicacao} e a divisão é {divisao}.')
 """