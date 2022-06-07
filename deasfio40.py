nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))

media = (nota1 + nota2) / 2

if media >= 7:
    print('APROVADO COM MÉDIA {}'.format(media))
elif media >= 5 and media <= 6.9:
    print('RECUPERAÇÃO, UMA VEZ QUE A MÉDIA FOI {}'.format(media))
else:
    print('REPROVADO, UMA VEZ QUE A MÉDIA FOI {}'.format(media))