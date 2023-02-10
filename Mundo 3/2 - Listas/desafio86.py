# Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.


matriz = [[], [], []]

for c in range (0,3):
    for l in range (0,3):
        userNumber = int(input(f'Digite o número da {c,l}:'))
        matriz[c].append(userNumber)
for c in range (0,3):
    for l in range (0,3):
        print(f'[{matriz[c][l]:^5}]', end='')
    print()