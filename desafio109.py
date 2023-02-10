# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
import moeda109

userMoeda = int(input('Digite um valor: '))

print(f'A metade de R${userMoeda} é R${moeda109.metade(userMoeda, True)}')
print(f'O dobro de R${userMoeda} é R${moeda109.dobro(userMoeda, True)}')
print(f'Com o desconto de 10% no R${userMoeda}, o valor final é R${moeda109.diminuir(userMoeda, 10, True)}')
print(f'Com o aumento de 10% no R${userMoeda}, o valor final é R${moeda109.aumentar(userMoeda, 10, True)}')