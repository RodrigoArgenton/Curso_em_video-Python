from datetime import date
nasc = int(input('Digite o seu ano de nascimento: '))
ano = date.today().year
idade = ano - nasc

print('Você tem {} anos e está na categoria: '.format(idade))

if idade <= 9:
    print('MIRIM')
elif idade >= 10 and idade <= 14:
    print('INFANTIL')
elif idade >= 15 and idade <= 19:
    print('JUNIOR')
elif idade >= 10 and idade <= 25:
    print('SÊNIOR')
else:
    print('MASTER')