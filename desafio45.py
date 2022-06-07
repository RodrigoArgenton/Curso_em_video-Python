from random import randint
from time import sleep
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
jogador = int(input('''Escolha uma das seguites opções:
[ 0 ] pedra
[ 1 ] papel
[ 2 ] tesoura

Qual seria a opção? '''))

# O sleep espera é um contador em segundo que realiza a proxima função somente após pasar o tempo descrito
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

# print que multiplica as informações dentro do ('')
print('-=' * 30)

print('O computador escolheu: {}'.format(itens[computador]))
print('O jogador escolheu a opção: {}'.format(itens[jogador]))

# print que multiplica as informações dentro do ('')
print('-=' * 30)

# O JOGADOR ESCOLHEU PEDRA
if jogador == 0:
    if computador == 0:
        print('EMPATE')
    elif computador == 1:
        print('O JOGADOR PERDEU')
    elif computador == 2:
        print('O JOGADOR GANHOU')
    else:
        print('Valor invalido')

# O JOGADOR ESCOLHEU PAPEL
elif jogador == 1:
    if computador == 0:
        print('O JOGADOR GANHOU')
    elif computador == 1:
        print('EMPATE')
    elif computador == 2:
        print('O JOGADOR PERDEU')
    else:
        print('Valor invalido')

# O JOGAODR ESCOLHEU TESOURA
elif jogador == 2:
    if computador == 0:
        print('O JOGADOR PERDEU')
    elif computador == 1:
        print('O JOGADOR GANHOU')
    elif computador == 2:
        print('EMPATE')
    else:
        print('Valor invalido')
else:
    print('Valor invalido')