# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

teste = (input('Digite algo: '))
print(teste)
print('  ')
print(f'O que você digitou é do tipo: {type(teste)}')
print('Tem espaços?: ', teste.isspace())
print('É um número?: ', teste.isnumeric())
print('É alfabético?: ', teste.isalpha()) 
print('É alfanumérico?: ', teste.isalnum())
print('Todas as letras são maiúsculas?: ', teste.isupper())
print('Todas as letras são minúsculas?: ', teste.islower())
print('Está capitalizada (maiúscula e minúscula):? ', teste.istitle())





