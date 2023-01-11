number = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

userNumber = int(input('Digite um número entre 0 e 20: '))

#condicional de repetição, caso o valor fornetido seja diferente de 0 até 20
while userNumber < 0 or userNumber > 20:
    userNumber = int(input('O valor inserido está incorreto, por favor, digite um número entre 0 e 20: '))

print(f'Você digitou o número {number[userNumber]}')

