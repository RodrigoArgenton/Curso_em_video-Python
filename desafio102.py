# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(num, show=True):
    """
    -> Calcula fatorial de um número
    num: valor a ser calculado
    show: parâmetro com o objetivo de mostrar ou não a equação
    return: retorna resultado.  
    
    """
    result = 1
    cont = num
    while True:
        result *= cont
        if show == True:
            print(f'{cont}', end='')
            if cont != 1:
                print(' X ', end='')
            else:
                print(' = ', end='')
        cont -= 1
        if cont == 0:
            break
    return print(result)

numUser = int(input('Digite um número para mostrar o seu fatorial: '))
showUser = str(input('Show equação? [S/N] ')) .upper() .strip() [0]
while True:
    while showUser not in 'SN':
        showUser = str(input('Show equação? [S/N] ')) .upper() .strip() [0]
    if showUser in 'S':
        showUser = True
    else:
        showUser = False
    break
fatorial(numUser, showUser)