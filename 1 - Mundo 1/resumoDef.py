from time import sleep

class resumo:
    def __init__(self, palavra, frase, numero, fracao):
        '''
        Essa classe tem como finalidade, explicar processos basicos pelo interative help ou comentando atraves de prints e etc.
        Esse resumo é somente do mundo 1 do curso do gustavo guanabara.
        '''
        self.palavra = palavra
        self.frase = frase
        self.numero = numero
        self.fracao = fracao
        pass



    def imprimir(self):
        '''
        'Imprimir' tem como objetivo mostrar uma informação na tela e mostrar como funciona o processo de forma clara e rapida.
        Segue informações sobre todos as funções ou atributos utilziado: 

        int: recebe valor inteiro
        str: recebe valor do tipo string
        float: recebe valor do tipo fração
        print: imprime uma informações na tela
        '''

        styleLine()
        print(f'{"Função a seguir guarda um valor inserido pelo uruário em um local":^100}')
        styleLine()
        sleep(1)
        x = int(input('\nDigite um número inteiro: '))
        sleep(1)
        print('\n--Note que foi solicitado um número, e o mesmo foi informado que seria inteiro, sendo assim, foi utilizado metodo "int"')
        sleep(1)
        print('Exemplo do processo anterior: x = int(input("Digite um número inteiro: "))')
        sleep(1)
        print('--Sendo o x a variavel que recebeu o valor inserido pelo usuário')
        sleep(1)
        print('--int sendo o metodo para receber um valor inteiro')
        sleep(1)
        print('--input para receber um valor inserido pelo usuário')
        sleep(5)
        


def styleLine():
    print('+'*100)