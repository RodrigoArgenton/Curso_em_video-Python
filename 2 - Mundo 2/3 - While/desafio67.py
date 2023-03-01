#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

#laço de repetição com o objetivo de ler uma váriavel constamente e parar caso o valor inserido seja negativo
while True:
    numtabuada = (int(input('Digite um número para saber a sua tabiada: ')))
    #coloquei essa variavel dentro do laço, uma vez que pode ser executado várias vezes e achei essa forma a mais simples
    cont = 1

    #laço de parada caso seja um valor negativo
    if numtabuada < 0:
        break

    #laço que será realizado a tabuada
    print('--'*20)
    while cont != 11:
        print(f'{numtabuada:^5}X {cont:^5} = {numtabuada*cont:^5}')
        cont += 1
    print('--'*20)
print('Programa encerrado. VOLTE SEMPRE!')
