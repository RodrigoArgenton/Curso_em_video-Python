# Aprimore o desafio anterior, mostrando no final: 
# A) A soma de todos os valores pares digitados. 
# B) A soma dos valores da terceira coluna. 
# C) O maior valor da segunda linha.

matriz = [[], [], []]
allPairSum = 0
threeCSum = 0
twoCSum = 0

for c in range (0,3):
    for l in range (0,3):
        userNumber = int(input(f'Digite o número da {c,l}:'))
        if userNumber % 2 == 0:
            allPairSum += userNumber
        if l == 2:
            threeCSum += userNumber
        matriz[c].append(userNumber)
        if c == 1:
                if userNumber > twoCSum:
                    twoCSum = userNumber
print('+'*30)
for c in range (0,3):
    for l in range (0,3):
        print(f'[{matriz[c][l]:^5}]', end='')
    print()
print('+'*30)
print(f'A soma de todos os valores pares é: {allPairSum}')
print(f'A soma dos valores da terceira coluna é: {threeCSum}')
print(f'O maior valor da segunda linha é: {twoCSum}')