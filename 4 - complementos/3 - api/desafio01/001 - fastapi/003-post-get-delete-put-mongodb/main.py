from fastapi import FastAPI
from pydantic import BaseModel
from banco_de_dados import insert_db, get_db, del_db, put_db

class User(BaseModel): # Modelo de um usuário, onde consta as informações importantes do mesmo
    email: str
    senha: str
    nome: str
    idade: int | None = None

# nome da api
app = FastAPI()

@app.post("/") # path
async def cadastrar(cadastro: User): #função que cadastra um usuário e adiciona no mongodb
    insert_db(cadastro.dict())
    return {"Usuário": cadastro}

@app.get("/") # path
async def pegar_usuario(): #Função que mostra todos os cadastros do db
    all_users = get_db()
    return all_users

@app.delete("/delete/{email}") #path
async def deletar_usuario(email: str):
    delCond = del_db(email) #chamada defunção que realizar o processo de deletar usuário e retorna valor para verdade, se encontrar o usuário e falso para erro ou não encontrar
    if  delCond is True:
        return {"Mensagem": "Cadastro excluído com sucesso"}
    else:
        return {"Meensagem":"Cadastro não foi encontrado"}
    
@app.put("/update/{keyUser}/{usuario}/{keyValor}/{valor}") #path
async def alterar_usuario(keyUser: str, usuario: str, keyValor: str,valor: str):
    put_db({keyUser: usuario}, {keyValor: valor}) #função que encontra o usuário e altera o valor inserido pelo usuário.
    return {"Mensagem": "Usuário atualizado com sucesso."}