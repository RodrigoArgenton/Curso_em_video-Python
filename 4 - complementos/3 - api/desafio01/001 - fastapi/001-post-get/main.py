from fastapi import FastAPI
from pydantic import BaseModel

# Modelo de um usuário, onde consta as informações importantes do mesmo
class User(BaseModel):
    email: str
    senha: str
    nome: str
    idade: int | None = None

# nome da api
app = FastAPI()

# lista que armazena (temporariamente) os cadastros realizados no path("/")
results = []

# path
@app.post("/")
async def cadastrar(cadastro: User): #função que cadastra um usuário e adiciona na lista temoporária
    results.append(cadastro)
    return cadastro

# path
@app.get("/")
async def pegar_usuario(): #função que retorna todos os usuários cadastrados pela função "cadastrar"
    return results

