class tv:
    '''
    Classe com o objetivo de controlocar o volume, mostrar o volume atual e mudar o canal
    função:
    volume;
    print_volume;
    mudar_canal;
    '''
    def __init__(self, ligar=False, desligar=False, canal=0, volumeatual=0):
        '''
        função inicial para começar a classe.
        '''
        self.ligar = ligar
        self.desligar = desligar
        self.canal = canal
        self.volumeatual = volumeatual
        print(f'status atual da tv: {self.ligar}')

    def volume(self, aumentar=0, diminuir=0):
        '''
        aumentar ou diminuor o volume

        parametros:
        aumentar;
        diminuir;
        '''
        while self.volumeatual + aumentar > 100:
            aumentar = int(input(f'O valor inserido {aumentar} ultrapassa o volume 100, uma vez que o volume atual é {self.volumeatual}, logo, por favor insira um valor valido: '))
        self.volumeatual += aumentar
        while self.volumeatual - diminuir < 0:
            diminuir = int(input(f'O valor inserido {diminuir} ultrapassa o volume 100, uma vez que o volume atual é {self.volumeatual}, logo, por favor insira um valor valido: '))
        self.volumeatual -= diminuir

    def print_volume(self):
        '''
        mostra o volume atual
        '''
        print(f'O volume atual é: {self.volumeatual}')

    def mudar_canal(self, valor):
        '''
        muda o cananal dentro de uma faixa de 0 até 1000

        parametro:
        valor;
        '''
        while 0 >= valor <= 1000:
            valor = int(input('Canal não existe! digite outro canal: '))
        self.canal = valor
        print(f'Canal atual: {self.canal}')