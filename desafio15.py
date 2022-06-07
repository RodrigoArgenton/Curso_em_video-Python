dias = int(input('Qual seria a quantidade de dias que o carro foi alugado? '))
km = float(input('Quantos km o carro andou? '))
valordias = dias * 60
valorkm = km * 0.15
valortotal = valordias + valorkm
print('O valor a ser pago pela utilização do veiculo é: R${}.'.format(valortotal))