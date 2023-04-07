class login:
    def __init__(self, email, senha):
        self.email = email
        self.senha = senha
        self.sucesso = False

    def validacao(self):
        email = "teste@gmail.com"
        senha = "senha123"
        if email == self.email and senha == self.senha:
            self.sucesso = True
            print("sucesso.")
        else:
            print("E-mail ou senha incorreto.")
    
    def returnoValidacao(self):
        if self.sucesso == True:
            return True
        else:
            print("Error")