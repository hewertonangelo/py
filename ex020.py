numero = int(input('Digite um número: '))

n = str(numero)
print('Analisando o nº {}'.format(numero))
print('Unidade: {}'.format(numero // 1 % 10))
print('Dezena: {}'.format(numero // 10 % 10))
print('Centena: {}'.format(numero // 100 % 10))
print('Milhar: {}'.format(numero // 1000 % 10))