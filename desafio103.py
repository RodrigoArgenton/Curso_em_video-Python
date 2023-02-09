# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(jogador='<desconhecido>', gols=0):
    print(f'O jogador {jogador} fez {gols} gol(s) no campeonato')


jogador = str(input('Nome do jogador: ')) .strip() .upper()
nunGols = str(input('Numeros de gols: ')) .strip()

if nunGols.isnumeric():
    nunGols = int(nunGols)
else:
    nunGols = 0

while True:
    if len(jogador) + nunGols == 0:
        ficha()
    elif jogador == '' and nunGols >= 0:
        ficha(gols=nunGols)
    elif len(jogador) >= 1 and not nunGols:
        ficha(jogador)
    else:
        ficha(jogador,nunGols)
    break