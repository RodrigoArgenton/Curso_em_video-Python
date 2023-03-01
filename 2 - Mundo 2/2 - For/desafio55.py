#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

#Variavel de controle do maior e menor peso
maiorpeso = 0
menorpeso = 0

#laço de repetição com o objetivo de realizar as perguntas que ficação nas variaveis de controle e peso
for c in range(1, 6):
    peso = float(input("Digite o peso da pessoa número {}: ".format(c)))

#Condicional com o objetivo de receber o valor peso somente no primeiro laço
    if c == 1:
        maiorpeso = peso
        menorpeso = peso
#Condicional que irá realizar o processo de recebimento do maior ou menor peso conforme inserido pelo user
    else:
        if peso >= maiorpeso:
            maiorpeso = peso

        if peso <= menorpeso:
            menorpeso = peso

print("O maior peso foi: {}Kg".format(maiorpeso))
print("O menor peso foi: {}Kg".format(menorpeso))