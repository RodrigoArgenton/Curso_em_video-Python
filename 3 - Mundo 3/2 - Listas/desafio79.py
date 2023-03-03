#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
lista = []

condwhile = 'S'

while condwhile in 'S':
    usernumber = (int(input('Digite um número: ')))
    while usernumber in lista:
        usernumber = (int(input('O número digitado ja se encontra na lista, digite novamente: ')))
    lista.append(usernumber)
    condwhile = str(input('Deseja continua? [S/N] ')) .strip() .upper() [0]

print(f'Os número existentes na lista são: {sorted(lista)}')