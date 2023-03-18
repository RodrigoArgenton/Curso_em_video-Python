from dotenv import load_dotenv
from pymongo import MongoClient
from time import sleep
import json
import os
import requests


load_dotenv()   # carrega o arquivo .env
MONGO_URI = os.getenv("MONGO_URI")  # recebe o valor que está na variavel "MONGO_URI" que está no arquivo .env
cliente = MongoClient(MONGO_URI)    # encurta o processo de conexão com os bancos de dados existentes no mongo
banco = cliente.banco_desafio002    # cria um banco de dados chamado "banco_desafio002"
colecao = banco['desafio002']       # cria uma coleção no bando de dados "desafio002"

while True:
    request = requests.get('https://www.affirmations.dev/')

    c = colecao.insert_one(json.loads(request.content))
    print(request.content)
    cont = str(input('Deseja continua?[S/N] ')) .strip() .upper() [0]
    if cont == 'N':
        break

for document in colecao.find(): # mostra todos os dicionarios existentes
    print('-'*50)
    for a, b in document.items():
        print(f'{a}: {b}')
    print('-'*50)

sleep(15)
colecao.drop()