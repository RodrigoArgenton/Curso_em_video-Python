# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.
cores = [
        '\033[0;30;31m', #0-vermelho
        '\033[0;30;32m', #1-verde
        '\033[0;30;34m', #2-azul
        '\033[0;30;36m', #3-ciano
        '\033[0;30;35m', #4-magenta
        '\033[0;30;33m', #5-amarelo
        '\033[0;30;30m', #6-preto
        '\033[0;30;37m', #7-branco
]

def comando(com, cor=0):
    print(cores[cor], end='')
    help(com)
    print(cores[7], end='')

while True:
    com = str(input('Digite o comando que deseja ver: ')) .strip()
    if com.upper() in 'FIM':
        break
    comando(com, 5)
    