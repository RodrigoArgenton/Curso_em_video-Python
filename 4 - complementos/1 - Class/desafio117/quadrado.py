
class quadrado:
    '''
    Classe com as seguintes funções: calcular area, mudar valor e mostrar valor atual.
    Essa classe tem as seguintes funções:
    CalcularArea;
    MudarValor;
    ValorAtual;
    '''

    def __init__(self, tamanho):
        '''Setar o valor infomado na variavel tamanho, o mesmo só recebe um parametro que seria o tamanho do lado de um quadrado'''
        self.tamanho = tamanho

    def CalcularArea(self):
        '''
        Calcular o tamnho do quadrado conforme tamanho, o mesmo não precisa que seja passado parametros
        '''
        totalArea = self.tamanho * 2
        return print(totalArea)

    def MudarValor(self, newTamanho):
        '''
        Mudar o tamnho do lado do quadrado, essa função recebe um valor novo e seta ele na classe para possiveis chamadas de calculo. A função recebe um valor.
        '''
        self.tamanho = newTamanho
        return 'Valor alterado!'

    def ValorAtual(self):
        '''
        Printa o valor que está alocado na variavel tamanho. não recebe parametros.
        '''
        return print(f'O valor atual do lado do quadrado é: {self.tamanho}')
