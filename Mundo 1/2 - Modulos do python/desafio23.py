# programa com o objetivo de emitir a unidade, dezena, centena e milhar de um número qualquer.
# leitura do número
num = int(input('Digite um número: '))

# Forma matemática para realizar o processo.
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

# emissão de dados.
print('Analisando o primeiro número {}'.format(num))
print('unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
