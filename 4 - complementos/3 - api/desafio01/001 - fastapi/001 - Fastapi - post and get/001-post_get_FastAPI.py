from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    email: str
    senha: str
    nome: str
    idade: int | None = None

app = FastAPI()

results = []

@app.post("/")
async def cadastrar(cadastro: User):
    results.append(cadastro)
    return cadastro

@app.get("/")
async def pegar_usuario():
    return results

