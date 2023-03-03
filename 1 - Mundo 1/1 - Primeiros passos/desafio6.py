# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

# variavel para armazenar um valor inteiro
n1 = float(input('Digite um número: '))

# variaveis para realizar uma função de calculo, sendo elas: dobro, triplo e raiz de um valor
dobro = n1 * 2
triplo = n1 * 3
raiz = n1 ** 0.5

# print do resultado final
print(f'''O valor informado foi {n1}, logo:
dobro: {dobro}
triplo:{triplo}
raiz: {raiz}
''')