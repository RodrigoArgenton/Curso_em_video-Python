# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

# variavel de alocação de valor inserido pelo usuário
metros = float(input('Digite um valor: '))

# variaveis para calculo
centimetros = metros * 100
milimetros = metros * 1000

# imprime valores calculado
print(f'O valor inserido foi {metros:.0f} m, logo, o valor em centímetros é {centimetros:.0f} cm e em milimetros é {milimetros:.0} mm')