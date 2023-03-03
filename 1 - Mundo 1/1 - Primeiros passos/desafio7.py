# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

# variavel de recebimento de notas
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

# marivael de calculo com o objetivo de dividir as notas para pegar a media
media = (n1+n2) / 2

# imprime o resultado das notas e a media
print(f'A nota 1 foi {n1:.1f} e a nota 2 foi {n2:.1f}, sendo assim a media é: {media:.1f}')