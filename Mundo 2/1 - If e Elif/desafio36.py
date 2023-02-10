#entrada de valores
valor = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o seu salario: R$'))
ano = int(input('Digite a quantidade de anos para o financiamento: '))

#variaveis de calculo
mensal = valor / (ano * 12)
prestação = salario * (30 / 100)

#conficional de financiamento
if prestação >= mensal:
    print('Você está aprovado para comprar o apartamento e o valor mensal será de R${:.2f}.'.format(mensal))
else:
    print('infelzimente você não está habito para realizar o seu financiamento devido ao seu baixo rendimento, uma vez que o valor mensal é R${:.2f} e compromente a sua renda ultrapassando os 30%'.format(mensal))