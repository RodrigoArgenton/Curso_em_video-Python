real = float(input('QUanto de dinheiro você tem na sua carteira? R$'))
dolar = real / 5.12
euro = real / 6.06
print('Com R${:.2f} você pode comprar U${:.2f} ou comprar €{:.2f}'.format(real, dolar, euro))