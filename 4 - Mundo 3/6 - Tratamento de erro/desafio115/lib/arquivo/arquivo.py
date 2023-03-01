from lib.interface.funcao import *

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
    except:
        print('Houve algum problema na criação do arquivo.')
    else:
        print('Arquivo criado com sucesso!')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')

    except:
        print('Erro ao ler o arquivo...')
    
    else:
        cabecalho('PESSOAS LISTADAS NO BANCO DE DADOS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<35}{dado[1]:>2} anos')

def cadastrar(arquivo, nome='Desconhecido', idade=0):
    try:
        a = open(arquivo, 'at')
    except:
        print('Erro ao abrir o aquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Erro ao escrever no arquivo')
        else:
            print(f'{nome} adicionado')