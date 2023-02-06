# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint

def sorteia():
    gen = []
    for c in range(1, 6):
        gen.append(randint(1, 10))
    print(f'Os números sorteados foram: {gen} e temos {len(gen)}')
    return gen
def somaPar(soma):
    somaP = 0
    for v in soma:
        if v % 2 == 0:
            somaP += v
    print(f'Somando os valores os valores pares {sorted(number)}, temos: {somaP}')

number = sorteia()
somaPar(number)