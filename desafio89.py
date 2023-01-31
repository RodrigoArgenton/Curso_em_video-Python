#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

listaAlunos = list()

while True:
    nomeAluno = str(input('Digite o nome do aluno: '))
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    mediaAluno = (nota1 + nota2) / 2
    listaAlunos.append([nomeAluno,[nota1, nota2], mediaAluno])
    userCont = str(input('Deseja continuar? [S/N] ')) .strip() .upper() [0]
    if userCont in 'N':
        break

print(f'{"N°":<3}{"Nome":<8}{"Média":>8}')
for i, a in enumerate(listaAlunos):
    print(f'{i:<2}{a[0]:<10}{a[2]:>8.1f}')

while True:
    userNotaAluno = int(input('Deseja ver a nota de qual aluno? para encerrar digite 999'))
    if userNotaAluno <= len(listaAlunos) - 1:
        print(f'O aluno {listaAlunos[userNotaAluno - 1][0]} tirou na primeira nota {listaAlunos[userNotaAluno - 1][1][0]} e na segunda {listaAlunos[userNotaAluno - 1][1][1]}')
    if userNotaAluno == 999:
        break