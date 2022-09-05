#Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.


from ftplib import parse227
from time import sleep

print('Olá, sou um progrma que mostra os 10 primeiros termos de um PA, o que acha de experimentar ?')
sleep(2)

#variavel com o objetivo de realizar a PA, lembrando que o primeiro termo é o valor inicial da PA e a razão é a soma que será realizada após o primeiro termo, por exemplo, se tivermos o primeiro termo como 2 e a razão como 1, a razão irá somar o seu valor com o primeiro termo, sendo assim, irá começar com 2, o segundo termo será 3, o terceiro será 4 e assim vai.
primeirotermo = int(input('Digite o primeiro termo de uma PA: '))
razao = int(input('Agora, digite a razão desta PA: '))

pa = 10

#laço de repetição com o objetivo de realizar o processo de uma PA
while pa != 0:
    #sleep(1)
    print(' {} ->'.format(primeirotermo), end='')
    primeirotermo += razao
    pa -= 1
    if pa == 0:
        print(' FIM')
        maispa = int(input('Quantos termos você deseja mostrar mais? caso digite 0, o programa irá encerrar. '))
        pa += maispa
        if maispa == 0:
            print('Foram mostrados {} termos de uma PA.'.format(maispa))
            print('Programa encerrado')