#Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.



def voto(nascimento):
    from datetime import datetime

    idade = datetime.now().year - nascimento

    if idade < 18 or idade > 65:
        return f'Você tem {idade} e o seu VOTO É OPCIONAL'
    elif idade < 16:
        return f'Você tem {idade} e o seu VOTO É NEGADO'
    else:
        return f'Você tem {idade} e o seu VOTO É OBRIGATÓRIO'

nasc = int(input('Digite o seu ano de nascimento: '))
print(voto(nasc))
