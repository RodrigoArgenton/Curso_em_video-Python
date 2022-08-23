#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

#Possibilita ver o ano que o usuário se encontra, desta forma, o software não ficará legado conforme primeira versão do sóftware
from datetime import date

#Variavel de contrale/quantidade de anos e quantidade de pessoas que são meiores ou menores de idade
maioridade = 0
menoridade = 0
anoatual = date.today().year

#Laço de repetição com o objetivo de criar 7 perguntas sobre a idade, juntamente com uma condicional com o objetivo de fazer a contagem de maiores e menores de idade
for c in range(1, 8):
    anouser = int(input("Digite a idade da {} pessoa: ".format(c)))
    idade = anoatual - anouser
    if idade >= 18:
        maioridade = maioridade + 1
    else:
        menoridade = menoridade + 1

#Resultado do user

print("A quantidade de pessoas maior de idade é: {}".format(maioridade))
print("A quantidade de pessoas menor de idade é: {}".format(menoridade))

#obs: o software antigo detinha erros que o tornava legado mais rápido, desta forma, conforme o professor guanabara explicou, o software se torna mais eficiente, uma vez que o ano é atualizado conforme a execução do progama.
