from random import choice

n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))

lista = [n1, n2, n3, n4]

print('Os alunos foram: \n {}, \n {}, \n {}, \n {}, \n e o aluno escolhido foi {}. '
      .format(n1, n2, n3, n4, choice(lista)))