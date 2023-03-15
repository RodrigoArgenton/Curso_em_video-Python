from dotenv import load_dotenv
from pymongo import MongoClient
import os

load_dotenv()   # carrega o arquivo .env
MONGO_URI = os.getenv("MONGO_URI")  # recebe o valor que está na variavel "MONGO_URI" que está no arquivo .env
cliente = MongoClient(MONGO_URI)    # encurta o processo de conexão com os bancos de dados existentes no mongo
meu_banco = cliente.banco_de_dados  # conecta no banco de dados
colecao = meu_banco['cientistas']   # cria uma collection, todavia, caso não seja inserido alguma informação, o mesmo é excluído posteriormente.

# cientista = [{"nome": "Oswaldo Cruz", "país": "BR"},
# {"nome": "Jaqueline Góes de Jesus", "país": "BR"},
# {"nome": "Anísio Teixeira", "país": "BR"},
# {"nome": "Suzana Herculano-Houzel", "país": "BR"},
# {"nome": "José Leite Lopes", "país": "BR"},
# {"nome": "Aroldo de Azevedo", "país": "BR"},
# {"nome": "Graziela Maciel Barroso", "país": "BR"},
# {"nome": "Edenise Garcia", "país": "BR"},]
# c = colecao.insert_many(cientista)

for document in colecao.find(): # mostra todos os dicionarios existentes
    print(document)
print()
print()
print('-'*50)

for a in colecao.find():    # mostra item por item dentro dos dicionários
    for b, c in a.items():
        print(f'{b}: {c}')
    print('-'*50)