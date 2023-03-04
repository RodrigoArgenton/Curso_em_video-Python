class contacorrente:
    ext = []
    def __init__(self, numConta, nome, saldo):
        self.numConta = numConta
        self.nome = nome
        self.saldo = saldo

    def alterarNome(self, newNome):
        self.nome = newNome
        return

    def deposito(self, valor):
        self.ext.append(+valor) #não mostra o sinal '+' no extrato
        self.saldo = self.saldo + valor
        print(f'Deposito concluido {self.nome}, saldo atual é: R${self.saldo}')
        contacorrente.printlinha()
        return

    def saque(self, retirada):
        if retirada > self.saldo:
            print(f'O seu saldo atual é R${self.saldo}, logo, não podera tirar o valor inserido.')
            contacorrente.printlinha()
        else:
            self.ext.append(-retirada)
            self.saldo = self.saldo - retirada
            print(f'Retirada de R${retirada} concluída. Saldo atual: R${self.saldo}')
            contacorrente.printlinha()

    def extrato(self):
        contacorrente.printlinha()
        print('+'*50)
        print(f"{'EXTRATO BANCARIO':^50}")
        print('+'*50)
        contacorrente.printlinha()
        for l in self.ext:
            if l < 0:
                print('Retirou: ', end='')
                print(f'{l:^13}')
            else:
                print('Depositou: ', end='')
                print(f'{l:^10}')
        contacorrente.printlinha()
        
    def printlinha():
        print()