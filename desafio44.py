valorproduto = float(input('Digite o valor do produto: R$'))


metodopagamento = int(input('''Escolha a forma de pagamento: 
    [ 1 ] a vista no dinheiro/cheque
    [ 2 ] a vista no cartão
    [ 3 ] no credito em até 2x
    [ 4 ] no credito acima de 3x
Digite a opção: '''))

vistadinheiro = valorproduto - (valorproduto * (10 / 100))
vistacartao = valorproduto - (valorproduto * (5 / 100))
cartao2x = valorproduto
cartao3x = valorproduto + (valorproduto * (20 / 100))


if metodopagamento == 1:
    print('O desconto é 10% e o valor do produto é R${}, logo, com desconte fica R${}.'.format(valorproduto, vistadinheiro))
elif metodopagamento == 2:
    print('O desconto é 5% e o valor do produto é R${}, logo, com desconte fica R${}.'.format(valorproduto, vistacartao))
elif metodopagamento == 3:
    print('O valor do produto é R${}.'.format(cartao2x))
elif metodopagamento == 4:
    print('O acrescimo é de 20% e o valor do produto é R${}, logo, com o acrescimo fica R${}.'.format(valorproduto, cartao3x))
else:
    print('Opção inserida incorreta')