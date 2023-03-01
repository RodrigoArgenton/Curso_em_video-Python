# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: 
# início, fim e passo. Seu programa tem que realizar três contagens através da função criada: 
# a) de 1 até 10, de 1 em 1 
# b) de 10 até 0, de 2 em 2 
# c) uma contagem personalizada
from time import sleep

def contador(inicioD, fimD, passoD):
    if passoD == 0:
        passoD = 1
    if inicioD > fimD and passoD >= 1:
        passoD *= -1
    print('=-='*20)
    print(f'Contador de {inicioD} até {fimD} pulando em {passoD}')
    sleep(2)
    for c in range(inicioD, fimD, passoD):
        sleep(0.5)
        print(f'{c} -> ', end='')
    sleep(0.5)
    print('FIM')
contador(1,10,1)
contador(10,0,-2)
print('=-='*20)
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)

