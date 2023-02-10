#importe de data
from datetime import date
ano = date.today().year

#solicitação de dados
nasc = int(input('Digite o seu ano de nascimento: '))
sexo = int(input('''Digite o valor a seguir dependendo do seu sexo:
    [ 1 ] Homem
    [ 2 ] Mulher
Qual seria a opção: '''))
idade = ano - nasc

print('Você nasceu em {} e tem {} no ano {}'.format(nasc, idade, ano))

#condicional de alistamento
if sexo == 1:
    if idade > 18:
        alistamento = nasc + 18
        print('Você ultrapassou {} anos do seu alistamento'.format(idade - 18))
        print('O ano que você deveria ter se alistado é: {}'.format(alistamento))
    elif idade < 18:
        plural = 18 - idade
        alistamento = nasc + 18
        if plural == 1 :
            print('Você tem que se alias em {} ano'.format(18 - idade))
            print('O ano que você precisa se alistar é: {}'.format(alistamento))
        else:
            print('Você tem que se alias em {} anos'.format(18 - idade))
            print('O ano que você precisa se alistar é: {}'.format(alistamento))
    else:
        print('Você tem {}, aliste-se ja!'.format(idade))
elif sexo == 2:
    print('O alistamento militar não é obrigatório para o sexo feminino.')
else:
    print('Valor inserido é invalido')