#Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120
from time import sleep

#variaveis com o bjetivo de realizar o processo de fatorial. obs: note que o resultado começou com "1" com o objetivo de realizar a multiplicação no while, uma vez que é necessário, caso contrário, ao multiplicar, o valor seria 0.
valorfatorial = int(input('Digite um número e descubra o seu fatorial: '))
resultado = 1
cont = valorfatorial

print('')
print('Calculando fatorial de {}! = '.format(valorfatorial), end='')

#Laço com o objetivo de realizar o fatorial
while cont > 0:
    
    sleep(0.5)
    print('{}'.format(cont), end='')
    
    if cont > 1:
        sleep(0.5)
        print(' X ',end='')
    else:
        sleep(0.5)
        print(' = ', end='')

    resultado = resultado * cont
    cont = cont - 1

sleep(1)
print('{}'.format(resultado))
print('')