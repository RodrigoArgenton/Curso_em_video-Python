# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.c

from random import randint
from operator import itemgetter

game = {}
ranking = []

game['Jogador1'] = randint(1,6)
game['Jogador2'] = randint(1,6)
game['Jogador3'] = randint(1,6)
game['jogador4'] = randint(1,6)

print('Valores sorteados: ')
for nome, resultado in game.items():
    print(f'{nome} tirou {resultado} no dado')
ranking = sorted(game.items(), key=itemgetter(1), reverse=True)

print('+'*50)
print(f'{"==RANKING DOS JOGADORES ==":^50}')
for i,v in enumerate(ranking):
    print(f'        {i+1}° lugar: {v[0]} tirou {v[1]} no dado.')