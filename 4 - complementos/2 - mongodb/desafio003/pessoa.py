class pessoa:
    def __init__(self):
        nome = str(input('Digite o seu nome: '))
        idade = int(input('Digite a sua idade: '))
        altura = int(input('Digite a sua altura em cm: '))
        peso = int(input('Digite o seu peso: '))
        sexo = str(input('Digite o seu sexo: '))
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
        self.sexo = sexo

    def mongodb(self):
        p = {}
        p['nome'] = self.nome
        p['idade'] = self.idade
        p['altura'] = self.altura
        p['peso'] = self.peso
        p['sexo'] = self.sexo
        print(p)
        return p
    