#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

vitorias = 0

print('=+'*30)
print('VAMOS JOGAR UM JOGO DE PAR OU IMPAR!!!')
print('=+'*30)

#laço de repetição com o objetivo de realizar um loop caso o user ganhe do computador
while True:
    usernum = int(input('Digite um número: '))
    userjogo = ' '
    while userjogo not in 'PI':
        userjogo = str(input('Digite P para PAR e I para IMPAR: ')) .strip() .upper() [0]
    compnum = randint(1,10)
    soma = usernum + compnum
    print('*-'*30)
    if soma % 2 == 0:
        print(f'Você jogou {usernum} e o camputador jogou {compnum}. Totalizando {soma}, logo deu PAR')
    else:
        print(f'Você jogou {usernum} e o camputador jogou {compnum}. Totalizando {soma}, logo deu IMPAR')
    print('*-'*30)
    if soma % 2 == 0 and userjogo == 'P' or soma % 2 == 1 and userjogo == 'I':
        print('Você venceu!')
        print('Vamos jogar novamente...')
        vitorias += 1
    else:
        break
print('Você perdeu!')
print(f'GAME OVER!!! você venceu {vitorias} vezes')