#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.


produtos = ('Caneta', 2,
            'Caderno', 1.78,
            'Lápis', 5,
            'lapiseira', 7.63,
            'Livro', 11.29,
            'Borracha', 1.5,
            'Tesoura', 4)

print('-'*50)
print('|', end='')
print(f'{"LISTA DE PRODUTOS:":^48}',end='')
print('|')
print('-'*50)

for c in range(0, len(produtos)):
    if c % 2 == 0:
        print(f'|{produtos[c]:.<35}',end='')
    else:
        print(f'R${produtos[c]:>8.2f}', end='')
        print(f'{"|":>4}')
print('-'*50)