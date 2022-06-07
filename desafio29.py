from time import sleep
velocidade = int(input('Qual foi a velocidade que o motorista passou pelo radar? '))
if velocidade > 80:
    print('PROCESSANDO...')
    sleep(2)
    print('-=-' * 20)
    multa = (velocidade - 80) * 7
    print('O(a) Sr(a) será multado e o valor será de {} reais.'.format(multa))
    print('-=-' * 20)

else:
    print('-=-' * 20)
    print('Parabéns, não ultrapassou a velocidade permitida, logo, não haverá multa')
    print('-=-' * 20)