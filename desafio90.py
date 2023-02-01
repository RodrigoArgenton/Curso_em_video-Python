#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

alunoDic = {}

alunoDic['nome'] = str(input('Digite o nome do aluno: '))
alunoDic['media'] = float(input(f'Digite a média de {alunoDic["nome"]} '))
if alunoDic['media'] < 5:
    alunoDic['situacao'] = 'reprovado'
elif 5 >= alunoDic['media'] < 7:
    alunoDic['situacao'] = 'resuperação'
elif alunoDic['media'] >= 7:
    alunoDic['situacao'] = 'Aprovado'

print('+'*50)

for a, s in alunoDic.items():
    print(f'   -{a} é {s}')