# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)
def leiaint(n):
    while True:
        num = input(n)
        if num.isnumeric():
            return num
        else:
            print('\033[31mERRO! Digite um número válido\033[m')




n = leiaint('Digite um número: ')

print(f'O número digitado é: {n}')