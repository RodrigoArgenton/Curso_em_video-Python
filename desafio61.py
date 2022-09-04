#Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

from time import sleep

print('Olá, sou um progrma que mostra os 10 primeiros termos de um PA, o que acha de experimentar ?')
sleep(2)

#variavel com o objetivo de realizar a PA, lembrando que o primeiro termo é o valor inicial da PA e a razão é a soma que será realizada após o primeiro termo, por exemplo, se tivermos o primeiro termo como 2 e a razão como 1, a razão irá somar o seu valor com o primeiro termo, sendo assim, irá começar com 2, o segundo termo será 3, o terceiro será 4 e assim vai.
primeirotermo = int(input('Digite o primeiro termo de uma PA: '))
razao = int(input('Agora, digite a razão desta PA: '))

pa = 10

#laço de repetição com o objetivo de realizar o processo de uma PA
while pa != 0:
    sleep(1)
    print(' {} ->'.format(primeirotermo), end='')
    primeirotermo += razao
    pa -= 1
    if pa == 0:
        print(' FIM')
sleep(1)
print('')
print('O que é uma PA???? segue explicação: Uma progressão aritmética (PA) é uma sequência numérica que segue a lógica a seguir: um elemento é igual ao anterior somado com uma constante real. Assim, é uma propriedade das progressões aritméticas que a diferença entre dois termos consecutivos quaisquer tenha sempre o mesmo resultado. Esse resultado é chamado de razão. A soma dos termos de uma PA pode ser calculada de maneira fácil por meio de uma fórmula.')
sleep(1)
print('')
print('Caso tenha mais interesse sobre o assunto, segue link para entender melhor: https://mundoeducacao.uol.com.br/matematica/soma-dos-termos-uma-pa.htm#:~:text=Uma%20progress%C3%A3o%20aritm%C3%A9tica%20(PA)%20%C3%A9,tenha%20sempre%20o%20mesmo%20resultado.')
print('')