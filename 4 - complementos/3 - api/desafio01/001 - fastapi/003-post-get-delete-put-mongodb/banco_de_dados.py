from dotenv import load_dotenv
from pymongo import MongoClient
import os

load_dotenv() #Carrega as variaveis de ambiente
MONGO_URI = os.getenv("MONGO_URI") #atribuí o valor que está na varivel "MONGO_URI"
cliente = MongoClient(MONGO_URI) #realizando a conexão com o mongodb
db = cliente.cadastros # atribuindo (ou criando) o valor da db a uma variavel
colecao = db.allcadastros # atribuindo (ou criando) uma colecao

# Enviar o valor recebido para o mongodb
def insert_db(valor):
    return colecao.insert_one(valor)

# Envia todos os cadastros do mongodb
def get_db():
    result = []
    for dicionario in colecao.find({}, {"_id": 0}):
        result.append(dicionario)
    return result

# Função que deleta um usuário
def del_db(email):
    delCond = colecao.delete_one({"email": email})
    if delCond.deleted_count == 1:
        return True
    else:
        return False

#função que altera uma informação do usuário.
def put_db(userFind, updateUsuario):
    return colecao.find_one_and_update(userFind,{"$set":updateUsuario})
