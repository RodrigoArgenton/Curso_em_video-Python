# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint

resultMega = []
contgames = cont = 0
print('-'*50)
print(f"{'JOGOS DA MEGA SENA':^50}")
print('-'*50)
print()
qntGames = int(input('Digite a quantidade de jogos que serão jogados: '))
print()
print('-='*3, f'  SORTEANDO {qntGames} JOGOS', '-='*3)
print()
while True:
    while True:
        geradorNumber = randint(1,60)
        if geradorNumber not in resultMega:
            resultMega.append(geradorNumber)
            cont += 1
        if cont >= 6:
            print(f'Jogo {contgames+1}: {sorted(resultMega)}')
            resultMega.clear()
            cont = 0
            contgames += 1
            break
    if contgames >= qntGames:
        break
print()
print('+'*17, f'< BOA SORTE! >', '+'*17)