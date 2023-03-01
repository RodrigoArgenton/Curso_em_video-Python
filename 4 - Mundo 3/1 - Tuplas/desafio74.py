#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint


sortNumber = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))

print('Os números gerados foram: ', end='')
for s in sortNumber:
    print(f'{s} ', end=' ')

print(f'\nO maior número é: {max(sortNumber)}')
print(f'O menor número é: {min(sortNumber)}')