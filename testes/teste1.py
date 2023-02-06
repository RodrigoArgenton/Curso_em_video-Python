def contador(inicioD, fimD, passoD):
    for c in range(inicioD, fimD, passoD):
        print(f'{c} -> ', end='')
        if c == fimD - 1:
            print('FIM')

inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)