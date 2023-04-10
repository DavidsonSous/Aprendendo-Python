import math
numero = int(input('Digite um número: '))
raiz = math.sqrt (numero)
print (' ')
#print (f'A raíz quadrada de {numero} é igual a {raiz}')
print (f'A raíz quadrada de {numero} é igual a {math.ceil(raiz)}')