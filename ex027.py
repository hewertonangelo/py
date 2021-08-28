from random import randint
from time import sleep
computador = randint(0 , 5) #faz o computador sortear
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. tente advinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) #jogador tenta advinhar

print('Processando...')
sleep(3)

print('\nacertou miseravel\n' if jogador == computador else '\nHAHA, errou!\n')

print('o numero que pensei foi: ',computador)

