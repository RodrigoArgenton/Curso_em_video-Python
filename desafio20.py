from random import shuffle
nome1 = str(input('Digite o primeiro nome: '))
nome2 = str(input('Digite o segundo nome: '))
nome3 = str(input('Digite o terceiro nome: '))
nome4 = str(input('Digite o quarto nome: '))
nomealunos = [nome1, nome2,nome3, nome4]
shuffle(nomealunos)
print('Segue alunos que irão se apresentar: ')
print(nomealunos)