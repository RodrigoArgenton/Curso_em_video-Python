class tv:
    def __init__(self, ligar=False, desligar=False, canal=0, volumeatual=0):
        self.ligar = ligar
        self.desligar = desligar
        self.canal = canal
        self.volumeatual = volumeatual
        print(f'status atual da tv: {self.ligar}')

    def volume(self, aumentar=0, diminuir=0):
        while self.volumeatual + aumentar > 100:
            aumentar = int(input(f'O valor inserido {aumentar} ultrapassa o volume 100, uma vez que o volume atual é {self.volumeatual}, logo, por favor insira um valor valido: '))
        self.volumeatual += aumentar
        while self.volumeatual - diminuir < 0:
            diminuir = int(input(f'O valor inserido {diminuir} ultrapassa o volume 100, uma vez que o volume atual é {self.volumeatual}, logo, por favor insira um valor valido: '))
        self.volumeatual -= diminuir

    def print_volume(self):
        print(f'O volume atual é: {self.volumeatual}')

    def mudar_canal(self, valor):
        while 0 >= valor <= 1000:
            valor = int(input('Canal não existe! digite outro canal: '))
        self.canal = valor
        print(f'Canal atual: {self.canal}')