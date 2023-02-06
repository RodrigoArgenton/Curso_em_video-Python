# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from random import randint

def maior(*num):
    mai = 0
    for c,v in enumerate(num):
        for c,v in enumerate(v):
            if c == 0:
                mai = v
            elif v > mai:
                mai = v
    print('+' * 50)
    if mai == 0:
        print('A lista não tem nenhum valor, logo, não existe o maior valor.')
    if mai >= 1:
        print(f'Foram passados os seguintes valores: {sorted(num[0])}')
        print(f'O maior número é: {mai}')
def geradorNumber(vzs):
    gen = []
    for c in range(1, vzs + 1):
        gen.append(randint(1,10))
    return gen

for c in range(0, 7):
    aleatorioRandint = randint(0,10)
    number = geradorNumber(aleatorioRandint)
    maior(number)



