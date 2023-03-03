# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.


jogadorFutebol = {}
gols = []
infoJogadores = []

while True:
    jogadorFutebol['nome'] = str(input('Nome do jogador: ')) .upper() .strip()
    quantidadeParidas = int(input(f'Quantas partidas o {jogadorFutebol["nome"]} jogou: ')) 
    for q in range(1, quantidadeParidas + 1):      
        gols.append(int(input(f'    Quantidade de gols na partida {q}: ')))
        if q == 1:
            jogadorFutebol['total'] = 0
        jogadorFutebol['total'] += gols[q-1] 
    #pode ser usado o jogadorFutebol['total'] = sum(gols   )
    jogadorFutebol['gols'] = gols[:]
    infoJogadores.append(jogadorFutebol.copy())
    userConc = str(input('Deseja continuar? [S/N] ')) .upper() .strip() [0]
    jogadorFutebol.clear()
    gols.clear()
    if userConc in 'N':
        break
print('+' * 50)
print(f'{"COD":<5} {"NOME":<8} {"GOLS":^25} {"TOTAL":>5}')
print('-' * 50)
for k,v in enumerate(infoJogadores):
    print(f'{k:<5}{v["nome"]:<10}{str(v["gols"]):^25}{v["total"]:>5}')
print('-'*50)
while True:
    userDados = int(input('Deseja ver o dados de qual jogador? (digite 999 para parar) '))
    if userDados == 999:
        break
    elif userDados >= len(infoJogadores):
        print('VALOR INSERIDO ESTÁ ERRADO!')
    else:
        print(f'  --LEVANTAMENTO DO JOGADOR {infoJogadores[userDados]["nome"]}')
        for k,v in enumerate(infoJogadores[userDados]["gols"]):
            print(f'   No jogo {k+1} fez {v} gols')
        print('-'*50)
print(f'{"--PROGRAMA ENCERRADO--":^50}')