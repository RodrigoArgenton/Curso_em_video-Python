produto = float(input('Qual é valor do seu produto? R$'))
desconto = produto - (produto * 5 / 100)
print('O produto que custava R${:.2f}, na promoção com o desconto de 5% vai custar R${:.2f}'.format(produto, desconto))
