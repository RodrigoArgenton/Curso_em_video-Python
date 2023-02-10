# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogadorFutebol = {}
gols = []

jogadorFutebol['nome'] = str(input('Nome do jogador: '))
quantidadeParidas = int(input(f'Quantas partidas o {jogadorFutebol["nome"]} jogou: '))

for q in range(1, quantidadeParidas + 1):      
    gols.append(int(input(f'    Quantidade de gols na partida {q}: ')))
    if q == 1:
        jogadorFutebol['total'] = 0
    jogadorFutebol['total'] += gols[q-1] 
#pode ser usado o jogadorFutebol['total'] = sum(gols   )
jogadorFutebol['gols'] = gols
print('+'*50)
print(jogadorFutebol)
print('+'*50)
for c,v in jogadorFutebol.items():
    print(f'No campo {c} tem o valor {v}')
print('+'*50)
for c,v in enumerate(gols):
    print(f' => Na partida {c+1}, fez {v} gols.')