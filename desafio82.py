# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
listaGeral = []
listaImpar = []
listaPar = []

while True:
    userNumber = int(input('Digite um número: '))
    listaGeral.append(userNumber)
    if userNumber % 2 == 0:
        listaPar.append(userNumber)
    else:
        listaImpar.append(userNumber)
    userCont = str(input('Deseja continuar? [S/N] ')) .upper() .strip() [0]
    if userCont in 'N':
        break

print(f'Os valores digitados foram: {listaGeral}')
print(f'OS valores impares dessa lista foram: {listaImpar}')
print(f'Os valores pares dessa lista foram: {listaPar}')