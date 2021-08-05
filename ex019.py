nome = str(input('Digite seu nome: '))

print('o nome digitado foi: {}'.format(nome.upper()))
print('o nome em maísculo, fica: {}'.format(nome.lower()))
print('o nome tem: {} caracteres'.format(len(nome) - nome.count(' ')))
separar = nome.split()
print('o primeiro nome é: {} e tem {} letras:'.format(separar[0], len(separar[0])))
