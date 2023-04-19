from fastapi import FastAPI
from pydantic import BaseModel
from banco_de_dados import insert_db, get_db

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