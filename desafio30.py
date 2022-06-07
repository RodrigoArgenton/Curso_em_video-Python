from time import sleep
numero = int(input('Digite um número e saiba se o mesmo será IMPAR ou PAR: '))
resultado = numero % 2
if resultado == 0:
    print('PROCESSANDO EM 3...')
    sleep(1)
    print('PROCESSANDO EM 2...')
    sleep(1)
    print('PROCESSANDO EM 1...')
    sleep(1)
    print('=_=' * 20)
    print('O valor digitado é Par.')
    print('=_=' * 20)
else:
    print('PROCESSANDO EM 3...')
    sleep(1)
    print('PROCESSANDO EM 2...')
    sleep(1)
    print('PROCESSANDO EM 1...')
    sleep(1)
    print('=_=' * 20)
    print('O valor digitado é impar.')
    print('=_=' * 20)
print('O resultado é {}'.format(resultado))