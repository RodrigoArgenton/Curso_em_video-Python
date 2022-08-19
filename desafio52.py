#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

#Variável de solicitação de dados
nuser = int(input("Digite um número: "))

#Variável para controle de números divisiveis
cont = 0

#Laço de repetição com o objetivo de verificar se o número inserido é primo
for c in range(1, nuser + 1):
    if nuser % c == 0:
        cont = cont + 1

#Condicionais com o objetivo de emitir uma mensagem conforme valor inserido
if cont == 2: 
    print("")
    print("O número inserido é primo!!")
    print("")
    print("Para um número ser um número primo, precisa ser dividido somente por ele e 1, caso seja dividido por mais números, não é primo.")
else:
    print("")
    print("O número inserido não é primo.")
    print("")
    if nuser == 1:
        print("A definição de número primo diz que primo é todo número natural que é divisível por 1 e por ele mesmo e maior ou igual a dois. Logo, um não pode ser primo")
    else:
        print("Primos são os números inteiros positivos divisíveis por um e por eles mesmos.")
