from validacao import login

while True:
    # email = str(input("Digite o seu E-mail: "))
    # senha = str(input("Digite a sua senha: "))
    
    acesso = login(email='rodrigo@gmail.com', senha='senha')
    acesso.users()
    break
