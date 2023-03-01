class quadrado:
    def __init__(self, tamanho):
        self.tamanho = tamanho

    def CalcularArea(self):
        totalArea = self.tamanho * 4
        return print(totalArea)

    def MudarValor(self, newTamanho):
        self.tamanho = newTamanho
        return 'Valor alterado!'

    def ValorAtual(self):
        return print(f'O valor atual do lado do quadrado é: {self.tamanho}')
