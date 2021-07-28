salario = float(input('Qual é o salário do funcionário R$ '))

print('Um funcionário que ganhava R$ {}, com o aumento de 15%, vai ganhar R$ {:.2f}'.
      format(salario, (salario*0.15)+salario))