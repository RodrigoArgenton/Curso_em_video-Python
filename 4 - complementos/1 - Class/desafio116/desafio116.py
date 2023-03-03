# Classe Bola: Crie uma classe que modele uma bola:
# Atributos: Cor, circunferência, material
# Métodos: trocaCor e mostraCor
from bola import bola as bl

creatBola = bl('amarelo', 4, 'borracha')
creatBola.MostrarCor()
creatBola.TrocarCor('azul')
creatBola.MostrarCor()

# help(creatBola.__init__) Retorna erro no vscode, mas informa o help.
help(creatBola.TrocarCor)
help(creatBola.MostrarCor)
