#Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8

quantidadedetermos = int(input('Quantos termos de fibonacci dejesa mostrar? '))

#Contador de termo
totaltermo = quantidadedetermos

t1 = 0
t2 = 1

#condicional para o primeiro while.
condwhile = True

#while, realizei o código desta forma para realizar testes e entender melhor o processo, será interessante o mesmo ser assim em um sistema onde existe muita ramificação e deseja encerrar após chegar no final de alguma delas
while condwhile == True:

#Laço com o objetivo de realizar a sequência de fibonacci
    while quantidadedetermos != 0:
        print('{} -> '.format(t1), end='')
        t3 = t1 + t2
        t1 = t2
        t2 = t3
        quantidadedetermos -= 1

        #condicional com o objetivo de aumentar os termos emitidos ou encerrar o programa
        if quantidadedetermos == 0:
            print('')
            quantidadedetermos = int(input('Deseja mostrar mais termos? '))
            totaltermo += quantidadedetermos
            if quantidadedetermos == 0:
                condwhile = False

    print('FIM')
print('A quantidade de termos que foram emitidos é: {}'.format(totaltermo))