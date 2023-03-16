class view:
    def __init__(self):
        pass

    def visualizarOrganizado(self, colecao):
        print('-'*50)
        for a in colecao.find():    # mostra item por item dentro dos dicionários
            for b, c in a.items():
                print(f'{b}: {c}')
            print('-'*50)

    def visualizarDados(self, colecao):
        print('+'*50)
        for document in colecao.find(): # mostra todos os dicionarios existentes
            print(document)
        print('+'*50)