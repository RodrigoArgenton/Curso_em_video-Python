# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
import moeda107

userMoeda = int(input('Digite um valor: '))

print(f'A metade de R${userMoeda} é R${moeda107.metade(userMoeda)}')
print(f'O dobro de R${userMoeda} é R${moeda107.dobro(userMoeda)}')
print(f'Com o desconto de 10% no R${userMoeda}, o valor final é R${moeda107.diminuir(userMoeda)}')
print(f'Com o aumento de 10% no R${userMoeda}, o valor final é R${moeda107.aumentar(userMoeda)}')