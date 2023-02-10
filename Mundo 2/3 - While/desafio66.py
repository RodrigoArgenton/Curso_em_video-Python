#Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag). (precisa utilizar o break)

#variaveis de adição unitária e soma
cont1 = 0
total1 = 0

#laço de repetição com o objetivo de usar o break
while True:
    num1 = int(input('Digite um número [Digite 999 para parar]: '))
    #condicional com o objetivo de parar o laço while caso a flag seja acionada
    if num1 == 999:
        break
    cont1 += 1
    total1 += num1
#note que foi atualizado o fstring se comparado aos exercicios anteriores
print(f'A soma dos {cont1} digitados é: {total1}')