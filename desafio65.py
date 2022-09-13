#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

from time import sleep


continuar = 'S'
qtdvalor = 0
soma = 0


while continuar in 'S':
    valor = int(input('Digite um número: '))
    qtdvalor += 1
    soma += valor
    if qtdvalor == 1:
        menor = maior = valor
    if menor > valor or valor > maior:
        if menor > valor:
            menor = valor
        else:
            maior = valor
    continuar = str(input('Deseja continua? [S/N] ')) .strip() .upper() [0]
        
media = soma / qtdvalor
print('Você Digitou {} números e a média é: {}'.format(qtdvalor, media))
print('O maior valor foi {} e o menor valor foi {}'.format(maior,menor))
