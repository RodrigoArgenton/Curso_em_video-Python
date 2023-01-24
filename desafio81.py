# Crie um programa que vai ler vários números e colocar em uma lista. 
# Depois disso, mostre: 
# A) Quantos números foram digitados. 
# B) A lista de valores, ordenada de forma decrescente. 
# C) Se o valor 5 foi digitado e está ou não na lista.
userLista = []

while True:
    userLista.append(int(input('Digite um número: ')))
    userCont = str(input('Deseja continuar? [S/N] ')) .strip() .upper() [0]
    if userCont == 'N':
        break

print(f'Os número digitados na lista forma:{userLista}')
print(f'Foram digitados {len(userLista)} numeros.')
print(f'Segue lista ordenada de forma decrescente: {sorted(userLista, reverse=True)}')

if 5 in userLista:
    print('O 5 faz parte da lista!')
else:
    print('O 5 não faz parte da lista!')