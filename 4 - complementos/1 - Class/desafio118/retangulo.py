from math import ceil


class retangulo:
    '''
    Realizar calculo e mostrar valor de um retangulo.
    '''
    def __init__(self, ladoA, ladoB):
        '''
        Parametros:
        ladoA e ladoB: recebe valores do retangulo
        '''
        self.ladoA = ladoA
        self.ladoB = ladoB

    def mudarValor(self, newLadoA, newLadoB):
        '''
        Muda o valores do lado do retangulo:
        newLadoA e newLadoB: recebe novos valores do retangulo
        '''
        self.ladoA = newLadoA
        self.ladoB = newLadoB
        return print('Valores alterados.')

    def mostrarLados(self):
        '''Printa os lados'''
        return print(f'Os lados são {self.ladoA}m e {self.ladoB}m')

    def calcularArea(self):
        '''Calcula a area do retangulo'''
        self.resultado = self.ladoA * self.ladoB
        return print(f'A area desse retangulo é: {self.resultado}m²')

    def calcularPerimetro(self):
        '''Calcula o perimetro do retangulo'''
        self.perimetro = 2 * (self.ladoA + self.ladoB)
        return print(f'O perimetro desse local é: {self.perimetro}m²')

    def calcularPisos(self):
        '''Calcula a quantidade de pisos em um perimetro'''
        pisos = self.perimetro / self.resultado
        return print(f'Serão necessário {ceil(pisos)} pisos para colocar no perimetro {self.perimetro}m²')

    # def calcularPisosV2(self, areaA, areaB):
    #     resultadoV2 = areaA * areaB
    #     pisos = resultadoV2 / self.resultado
    #     return print(f'Serão necessário {ceil(pisos)} pisos para colocar no perimetro {resultadoV2}m²')
