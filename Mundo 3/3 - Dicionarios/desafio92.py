# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import datetime

pessoa = {}

while True:
    pessoa['nome'] = str(input('nome: '))
    anoNascimento = int(input('Data de nascimento: '))
    pessoa['idade'] = datetime.now().year - anoNascimento
    pessoa['carteria'] = int(input('carteira de trabalho: (0 = não tem) '))
    if pessoa['carteria'] != 0:
        pessoa['contratacao'] = int(input('Ano de contratação: '))
        pessoa['salario'] = float(input('Remuneação: '))
        pessoa['aposentadoria'] = (pessoa['contratacao'] + 35 + pessoa['idade']) - datetime.now().year 
        break
    break
print('+'*50)
for k,v in pessoa.items():
    print(f'   -{k} tem o valor {v}')