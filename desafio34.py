salario = float(input('QUal seria o salario do fundionário? R$'))
if salario >= 1250:
    salario = (salario * 0.10) + salario
    print('O salario atual com o aumento de 10% é {}'.format(salario))
else:
    salario = (salario * 0.15) + salario
    print('O salario atual com o aumento de 15% é {}'.format(salario))