# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
# A) Quantas pessoas foram cadastradas 
# B) A média de idade 
# C) Uma lista com as mulheres 
# D) Uma lista de pessoas com idade acima da média


cadPessoa = {}
infoPessoa = []
soma = media = 0

while True:
    cadPessoa.clear()
    cadPessoa['nome'] = str(input('Nome: '))
    while True:
        cadPessoa['sexo'] = str(input('Sexo: [M/F] ')) .upper() .strip() [0]
        if cadPessoa['sexo'] in 'MF':
            break
        print('O valor digitado não é valido!')
    cadPessoa['idade'] = int(input('Idade: '))
    userContinuar = str(input('Deseja continuar? [S/N] ')) .upper() .strip() [0]
    soma += cadPessoa['idade']
    infoPessoa.append(cadPessoa.copy())
    

    while userContinuar not in 'SN':
        userContinuar = str(input('Deseja continuar? [S/N] ')) .upper() .strip() [0]
    if userContinuar == 'N':
        break
media = soma / len(infoPessoa)

print('+' * 50)
print(f'Ao todo, tem {len(infoPessoa)} pessoas cadastradas.')
print(f'A média da idade das pessoas é: {media}')
print('As seguintes pessoas são mulheres: ', end='')
for p in infoPessoa:
    if p['sexo'] in 'F':
        print(f'{p["nome"]}; ', end='')
print()
print('As seguintes pessoas estão com idades acima da média: ')
for p in infoPessoa:
    if p['idade'] >= media:
        print(f'{p["nome"]} com {p["idade"]}')