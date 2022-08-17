#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

#Variavel com o objetivo de verificar a quantidade de laços que será realizada
qtdlaco = int(input("Digite a quantidade de números que deseja informar: "))

#Declaração de variável - variável que detém a soma dos números pares
vf = 0

#Laço de repetiçãi que realiza o precesso de perguntar e somar os números pares 6 vezes
for c in range (1, qtdlaco + 1):
    valor = int(input("Digite um valor: "))
    if valor % 2 == 0:
        vf = valor + vf

#Print do resultado final
print("")
print(20*"+-")
print("A soma de todos os valores pares é : {}".format(vf))
print(20*"+-")
print("") 