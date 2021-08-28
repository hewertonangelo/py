from time import sleep

velocidade = float(input('Qual a sua velocidade? '))
padrao = int(80)
res = int(0)

if velocidade > 80:
    res = (velocidade - padrao) * 7
    print('Processando...')
    sleep(3)
    print('A sua velocidade foi {}KM/h e voce foi multado em R$ {}'.format(velocidade, res))

print('continue dirigindo com segurança')
