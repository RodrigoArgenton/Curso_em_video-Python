'''Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''

#Variavel com o objetivo de armazenar dois valores que serão somados, multiplicado ou verificar qual seria o maior
v1 = int(input('Digite o primeiro número: '))
v2 = int(input('Digtite o segundo número: '))

#variavel com o objetivo de iniciar o laço, caso contrário, a opção não terá nenhuma informação que ocasiona no não iniciamento do while
opcao = 0

#Laço com o objetivo de realizar a "CALCULADORA SIMPES"
while opcao != 5:
    print('''CALCULADORA SIMPLES!
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa''')
    opcao = int(input('Qual a sua opção? '))

#Condicionais com o objetivo de realizar o processo conforme usuário solicitou
    if opcao == 1:
        soma = v1 + v2
        print('A soma dos dois valores é: {}'.format(soma))
    elif opcao == 2:
        multiplicar = v1 * v2
        print('A multiplicação dos dois valores é: {}'.format(multiplicar))
    elif opcao == 3:
        if v1 > v2:
            print('O valor maior é: {}'.format(v1))
        elif v2 > v1:
            print('O valor maior é: {}'.format(v2))
        else:
            print('Os valores inserido são iguais!')
    elif opcao == 4:
        print('Computando...')
    else:
        print('Valor inserido está incorreto, digite novamente, por favor.')
    print('+-'*20)
    print('')