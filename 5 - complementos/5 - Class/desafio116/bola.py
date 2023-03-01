class bola:
    '''
    Classe que irá modelar uma bola com inserir e alterar cor
    '''

    def __init__(self, cor, circunferencia, material):
        '''
        função com o objetivo de pegar todas as informações básicas de uma bola
        Parametros:
            cor: cor da bola
            Circunferencia: pegar o valor da cicunferencia da bola
            material: Pegar uma str referente ao material da bola
        '''
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def TrocarCor(self, newCor):
        '''Trocar a cor da bola, o parametro é informado na função __init__'''
        self.cor = newCor

    def MostrarCor(self, mostrarTudo=False):
        '''
        Mostrar informações da bola, o mesmo tem duas saídas possíveis,
        mostrar somente a cor ou mostrar todas as informações que foram
        gravadas no __init__ e atualizadas, caso tenha utilizado a função
        TrocarCor'''
        if mostrarTudo is True:
            return print(f'''\nInformações da bola:
            Cor: {self.cor}
            circunferencia: {self.circunferencia}
            Material: {self.material}
            ''')
        return print(f'A cor da bola é: {self.cor}')
