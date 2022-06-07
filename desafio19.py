from random import choice
nome1 = str(input('Digite o nome do primeor aluno: '))
nome2 = str(input('Digite o nome do segundo aluno: '))
nome3 = str(input('Digite o nome do terceiro aluno: '))
nome4 = str(input('Digite o nome do quarto aluno: '))
nomealuno = [nome1, nome2, nome3, nome4]
nomeescolhido = choice(nomealuno)
print('O nome escolhido para apagar o quadro é: {}.'.format(nomeescolhido))