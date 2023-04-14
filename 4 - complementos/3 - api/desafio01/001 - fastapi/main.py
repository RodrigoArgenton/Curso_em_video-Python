from fastapi import FastAPI

app = FastAPI()

vendas = {
    1: {"teste1": "teste01", "preço": 5, "Quantidade": 2},
    2: {"teste2": "teste02", "preço": 6, "Quantidade": 3},
    3: {"teste3": "teste03", "preço": 7, "Quantidade": 4},
    4: {"teste4": "teste04", "preço": 8, "Quantidade": 5},
    5: {"teste5": "teste05", "preço": 9, "Quantidade": 6},
}

@app.get("/")
def home():
    return {"Vendas": len(vendas)}

@app.get("/vendas/{id_venda}")
def get_venda(id_venda: int):
    return vendas[id_venda]