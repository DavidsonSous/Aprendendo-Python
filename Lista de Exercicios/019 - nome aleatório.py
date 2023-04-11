# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

import random
aluno1 = ('Digite o nome do aluno:')
aluno2 = ('Digite o nome do aluno:')
aluno3 = ('Digite o nome do aluno:')
aluno4 = ('Digite o nome do aluno:')

print (f'O aluno escolhido foi {random.randint(aluno1,aluno2,aluno3,aluno4)}')