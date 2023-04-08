class login:
    def __init__(self, email, senha):
        from dotenv import load_dotenv
        from pymongo import MongoClient
        import os
        load_dotenv()   # carrega o arquivo .env
        MONGO_URI = os.getenv("MONGO_URI")  # recebe o valor que está na variavel "MONGO_URI" que está no arquivo .env
        cliente = MongoClient(MONGO_URI)    # encurta o processo de conexão com os bancos de dados existentes no mongo
        db = cliente.novouser
        colecao = db['users']
        self.colecao = colecao
        self.email = email
        self.senha = senha
        self.sucesso = False

    def validacao(self):
        for colecao in self.colecao.find():
            if colecao["email"] == self.email and colecao["senha"] == self.senha:
                self.sucesso = True
                print("sucesso.")
            else:
                print("E-mail ou senha incorreto.")
    
    def returnValidacao(self):
        if self.sucesso == True:
            return True
        else:
            print("Error")

    def novoUser(self):
        user = {}
        user['email'] = self.email
        user['senha'] = self.senha
        print(user)
        addcolecao = self.colecao.insert_one(user)