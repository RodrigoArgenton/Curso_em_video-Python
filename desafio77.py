#Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavra = (
    'estudar','cantar','amar','achar','aprender','correr','viver','partir','dividir','desistir'
)

for p in palavra:
    print(f'\nNa palavra {p.upper()} temos: ', end=(''))
    for letra in p:
        if letra in 'aeiou':
            print(f'{letra}',end=(' '))
