#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randrange

#Variavel com o objetivo de pegar um número aleatório entre 0 e 10
pcrandom = randrange(10)
conttentativas = 1

#Varivel com o objetivo de pegar o valor inserido pelo usuário que se encontra entre 0 e 10
jogador = int(input('''Gostaria de jogar um jogo?

Estou pensando em um número, dúvido você acertar!!

Digite um número entre 0 a 10 e tente adivinhar o número que pensei: '''))

#Laço de repetição com o objetivo de informar se a pessoa está perto do número que o computador pensou
while pcrandom != jogador:
    conttentativas += 1
    if pcrandom > jogador: 
        jogador = int(input('MAIS... Digite um palpite novamente: '))
    else:
        jogador = int(input('MENOS... Digite um palpite novamente: '))

#Resultado quando o usuário acertar
print('Parabéns, você acertou em {} tentativas.'.format(conttentativas))
