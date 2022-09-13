'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.'''

total = cont2 = quantidadeprodutosplus1000 = precomaisbarato = 0
nomemaisbarato = precoprodutosplus1000 = ' '

#laço com o objetivo de cadastramento infinito de produtos
while True:
    nomeproduto = str(input('Digite o nome do produto: '))
    precoproduto = float(input('Digite o preço do produto: '))
    cont2 += 1
    total += precoproduto

    #condicional com o objetivo contabilizar a quantidade de  item com o preço superior a 1000
    if precoproduto >= 1000:
        precoprodutosplus1000 = precoproduto
        quantidadeprodutosplus1000 += 1
    
    #condicional com o objetivo de realizar o processo de pegar o menor valor e o nome do produto
    if cont2 == 1:
        nomemaisbarato = nomeproduto
        precomaisbarato = precoproduto
    elif precomaisbarato > precoproduto :
        nomemaisbarato = nomeproduto
        precomaisbarato = precoproduto

    #condicional com o objetivo de repetir o laço, caso necessário
    cont = ' '
    while cont not in 'S/N':
        cont = str(input('Deseja continuar? [S/N] ')) .strip() .upper() [0]
    if cont == 'N':
        break

print('-------------------FIM DO PROGRAMA-------------------')
print(f'''Segue informações importantes: 
O preço total da compra é: {total:.2f}
{quantidadeprodutosplus1000} produtos custam mais que 1000 reais
O {nomemaisbarato} é o produto mais barato custando {precomaisbarato:.2f}
''')