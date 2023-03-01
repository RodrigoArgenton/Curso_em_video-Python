km = int(input('Qual seria a quantidade de kilometros que será realizado na viagem? '))
if km <= 200:
    custo = km * 0.50
    print('O valor a ser pago na viagem é de R$ {}'.format(custo))
else:
    custo = km * 0.45
    print('O valor a ser pago na viagem é de R$ {}'.format(custo))
