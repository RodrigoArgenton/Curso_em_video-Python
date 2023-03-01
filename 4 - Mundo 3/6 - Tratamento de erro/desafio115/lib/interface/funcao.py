def leiaint(n):
    while True:
        try:
            m = int(input(n))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número inteiro válido\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mPrograma interrompido pelo usuário\033[m')
            return 0
        else:
            return m

def linha(tam=42):
    return '-' * tam

def cabecalho(msg):
    print(linha())
    print(msg.center(42))
    print(linha())

def menu(lista):
    cabecalho('SISTEMA DE MENU')
    c = 1
    for item in lista:
        print(f'{cores[5]}{c}{cores[8]} - {cores[2]}{item}{cores[8]}')
        c+=1
    print(linha())
    opc = leiaint(f'{cores[1]}Sua opção: {cores[8]}')
    return opc

cores = [
        '\033[0;30;31m', #0-vermelho
        '\033[0;30;32m', #1-verde
        '\033[0;30;34m', #2-azul
        '\033[0;30;36m', #3-ciano
        '\033[0;30;35m', #4-magenta
        '\033[0;30;33m', #5-amarelo
        '\033[0;30;30m', #6-preto
        '\033[0;30;37m', #7-branco
        '\033[m',        #8-reseta
]