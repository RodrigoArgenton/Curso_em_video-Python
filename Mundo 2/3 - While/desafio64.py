#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

saida = soma = adicao = 0

#Laço de repetição com o objetivo de criar uma condicional onde soma, realiza a cotação etem uma flag para caso o user não queira continuar inserindo valor
while saida != 999:
    saida = int(input('Digite um número [999 para parar]: '))
    #condicional com o objetivo de soma e contabilizar os valores digitados
    if saida != 999:
        soma += saida
        adicao += 1
print('A soma de todos os numeros digitados é {} e a quantidade de numeros digitados é {}'.format(soma,adicao))
