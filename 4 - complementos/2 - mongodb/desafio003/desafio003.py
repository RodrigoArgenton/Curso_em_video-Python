from pessoa import pessoa
from dotenv import load_dotenv
from pymongo import MongoClient
import os

load_dotenv()   # carrega o arquivo .env
MONGO_URI = os.getenv("MONGO_URI")  # recebe o valor que está na variavel "MONGO_URI" que está no arquivo .env
cliente = MongoClient(MONGO_URI)    # encurta o processo de conexão com os bancos de dados existentes no mongo
db = cliente.banco_desafio003
colecao = db['desafio003']

print('+'*100)
print(f"|{'MENU PRINCIPAL':^98}|")
print('+'*100)

print(f"|{'1 - Cadastrar usuários':^98}|")
print(f"|{'2 - ver usuários cadastrados:':^98}|")
print('+'*100)
opcao = int(input('Qual seria a sua opção: '))

if opcao == 1:
    while True:
        pessoa1 = pessoa()
        addcolecao = colecao.insert_one(pessoa1.mongodb())
        continuar = str(input('Deseja continuar:[S/N] ')) .strip() .upper() [0]
        if continuar == 'N':
            break
elif opcao == 2:
    for itens in colecao.find():
        print('-'*100)
        for a,b in itens.items():
            print(f'{a}: {b}')
else:
    print('Valor não corresponde')






