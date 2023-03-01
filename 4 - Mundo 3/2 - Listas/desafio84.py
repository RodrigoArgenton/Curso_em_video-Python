# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre: 
# A) Quantas pessoas foram cadastradas. 
# B) Uma listagem com as pessoas mais pesadas. 
# C) Uma listagem com as pessoas mais leves.

cadastLista = []
bdLista = []
maiorPeso = menorPeso = 0


while True:
    cadastLista.append(str(input('Digite o seu nome: ')))
    cadastLista.append(float(input('Digite o seu peso: ')))
    if len(bdLista) == 0:
        maiorPeso = menorPeso = cadastLista [1]
    if cadastLista[1] > maiorPeso:
        maiorPeso = cadastLista[1]
    if cadastLista[1] < menorPeso:
        menorPeso = cadastLista[1]
    bdLista.append(cadastLista[:])
    cadastLista.clear()
    usercond = str(input('Deseja continuar? ')) .upper() .strip() [0]
    if usercond in 'N':
        break

print('+'*50)
print(f'Foram cadastradas {len(bdLista)} pessoas.')
print(f'O maior peso foi {maiorPeso}kg. As pessoas com maiores pesos foram: ', end='')
for nomePessoa in bdLista:
    if nomePessoa[1] == maiorPeso:
        print(f'[{nomePessoa[0]}]', end='')
print()
print(f'O menor peso foi {menorPeso}kg. As pessoas com menores pesos foram: ', end='')
for nomePessoa in bdLista:
    if nomePessoa[1] == menorPeso:
        print(f'[{nomePessoa[0]}]')