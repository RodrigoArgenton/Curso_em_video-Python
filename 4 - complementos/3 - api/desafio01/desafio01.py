from validacao import login

while True:
    email = str(input("Digite o seu E-mail: "))
    senha = str(input("Digite a sua senha: "))
    
    acesso = login(email, senha)
    acesso.validacao()
    
    if acesso.returnoValidacao() == True:
        break