# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(lag,comp):
    a = lag * comp
    print(f'A área de um terreno {lag} X {comp}  é {a}m²')
def linha():
    print('-'*50)

linha()
print(F'{"CONTROLE DE TERRENOS":^50}')
linha()

a = float(input('Digite a largura: '))
c = float(input('Digite o comprimento: '))
area(a,c)
