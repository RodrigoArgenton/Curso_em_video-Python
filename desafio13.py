salario = float(input('Qual seria o salario do funcionário? R$'))
acrescimo = salario + (salario * 15 / 100)
print('O funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}.'.format(salario, acrescimo))
