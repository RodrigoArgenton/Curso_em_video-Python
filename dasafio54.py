#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

maioridade = 0
menoridade = 0

for c in range(1, 7):
    idade = int(input("Digite a idade da {} pessoa: ".format(c)))
    if idade <= 2004:
        maioridade = maioridade + 1
    else:
        menoridade = menoridade + 1
print("A quantidade de pessoas maior de idade é: {}".format(maioridade))
print("A quantidade de pessoas menor de idade é: {}".format(menoridade))