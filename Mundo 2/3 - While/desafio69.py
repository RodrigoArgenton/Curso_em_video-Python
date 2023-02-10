''' Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
    A) quantas pessoas tem mais de 18 anos.
    B) quantos homens foram cadastrados.
    C) quantas mulheres tem menos de 20 anos.'''

geralmais18 = cadastradohomem = mulherermenos20 = 0

#laço de repetição com o objetivo de realizar o cadastro até o user terminar
while True:
    print('--'*20)
    print('CADASTRE UMA PESSOA')
    print('--'*20)

    idade = int(input('Idade: '))
    #variavel e laço de repetição que verifica o valor inserido pelo user, caso não seja M ou F, será realizado a repetição da pergunta
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')) .strip() .upper() [0]

    if idade >= 18:
        geralmais18 += 1
    if sexo == 'M':
        cadastradohomem += 1
    if sexo == 'M' and idade <= 20:
        mulherermenos20 += 1
    #variavel e laço de repetição que verifica o valor inserido pelo user, caso não seja S ou N, será realizado a repetição da pergunta
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Deseja continuar [S/N]: ')) .strip() .upper() 
    if cont == 'N':
        break

print('--'*20)
print(f'''Segue informações:
Quantidade de pessoas maiores de 18: {geralmais18}
Quantidade de homens cadastrados: {cadastradohomem}
Quantidade de mulheres com menos de 20: {mulherermenos20}''')