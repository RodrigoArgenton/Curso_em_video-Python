#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

s = []

for c in range(0,5):
    s.append(int(input(f'Digite um valor para a posição {c}: ')))


print(f'Os valores digitados foram: {s}')
print(f'O maior valor foi {max(s)} e está na posição: ', end='')
for p, v in enumerate(s):
    if v == max(s):
        print(f' {p}.', end='')
print()
print(f'O menor valor é {min(s)} e está na posição: ', end='')
for p, v in enumerate(s):
    if v == min(s):
        print(f' {p}.', end='')