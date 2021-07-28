nome = input('Nome do aluno:')

nota1 = float(input('Digite a primeira nota do aluno:'))
nota2 = float(input('Digite a segunda nota do aluno:'))

#{:.1f} - significa que:
#todo o numero so será reprensentado, um digito após o nº flutuante

print('a nota total do {} foi {:.1f}\ne, a sua média foi {:.1f}'. format(nome, (nota1 + nota2), (nota1 + nota2)/2 ))