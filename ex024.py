nome = str(input('Digite um nome: ')).strip().lower()

print('a letra A aparece {} vezes no nome'.format(nome.count('a')))
print('A primeira vez que ela aparece é na posição de nº {}'.format(nome.find('a')+1))
print('A ultima vez que ela aparece é na posição de nº {}'.format(nome.rfind('a')+1))