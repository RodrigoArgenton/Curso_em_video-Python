# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável. 
# Ex: escreva(‘Olá, Mundo!’) 
# Saída: 
# ~~~~~~~~~~~ 
# Olá, Mundo! 
# ~~~~~~~~~~~

def escreva(fraseD):
    numberfraseD = len(fraseD) + 2
    print('~' * numberfraseD)
    print(f'{fraseD:^{numberfraseD}}')
    print('~' * numberfraseD)

escreva('olá mundo')
escreva('Estudando Python')
escreva('Gustavo Guanabara')