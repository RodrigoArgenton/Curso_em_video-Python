from random import randrange
from time import sleep

print('-=-' * 20) #multiplica o valor dentro do print

pergunta = int(input('Vamos jogar um game onde o objetivod é acertar o numero que "pensei"? (digite 1 para "SIM" e 2 para "NÃO")')) #condição com o objetivo de saber se o player jogará

print('-=-' * 20) #multiplica o valor dentro do print

if pergunta == 1: #caso o valor seja 1, o jogador será inserido nesse "if" e começará o jogo.
    inteirojogador = int(input('Perfeito, para começar, digite um número entre 0 e 5: '))

else:
    print('Entendo, agradeço o feedback e volte sempre.') #print com o objetivo de encerramento.
    exit() #comando para encerrar o código.

pcrandon = randrange(6) #comando para sortear um número de 0 a 5.

#resultado final.
if pcrandon == inteirojogador:
    print('PROCESSANDO...')
    sleep(2)
    print('-=-' * 20)
    print('Parabens o número é igual ao inserido pelo computador.')
    print('-=-' * 20)

else:
    print('PROCESSANDO...')
    sleep(2)
    print('Infelizmente os números não foram iguais, uma vez que o valor digitado foi {} e o computador inseriu {}'.format(inteirojogador, pcrandon))