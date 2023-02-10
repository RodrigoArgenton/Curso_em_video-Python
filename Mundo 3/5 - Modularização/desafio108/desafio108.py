# Adapte o código do desafio 108moeda108, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
import moeda108

userMoeda = int(input('Digite um valor: '))

print(f'A metade de {moeda108.moeda(userMoeda)} é {moeda108.moeda(moeda108.metade(userMoeda))}')
print(f'O dobro de {moeda108.moeda(userMoeda)} é {moeda108.moeda(moeda108.dobro(userMoeda))}')
print(f'Com o desconto de 10% no {moeda108.moeda(userMoeda)}, o valor final é {moeda108.moeda(moeda108.diminuir(userMoeda))}')
print(f'Com o aumento de 10% no {moeda108.moeda(userMoeda)}, o valor final é {moeda108.moeda(moeda108.aumentar(userMoeda))}')