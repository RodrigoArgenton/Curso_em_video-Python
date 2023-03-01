#criar um menu em Python, usando modularização.




from lib.interface.funcao import *
from lib.arquivo.arquivo import *
from time import sleep

arq = 'BancoDeDados.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)
while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar pessoas', 'Sair'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho('Cadastrar uma pessoa')
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do sistema...')
        break
    else:
        print(f'{cores[0]}ERRO, digite uma opção valida!.{cores[8]}')
    sleep(2)