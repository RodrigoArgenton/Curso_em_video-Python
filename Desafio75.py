#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.

numb = (
    int(input('Digite um número: ')),
    int(input('Digite outro número: ')),
    int(input('Digite mais um número: ')),
    int(input('Digite o ultimo número: '))
)

print(f'Você digitou os seguintes números: {numb}')
print(f'O número 9 apareceu: {numb.count(9)} vezes')
if 3 in numb:
    print(f'O número 3 foi digitado na posição: {numb.index(3)+1}°')
else:
    print(f'Não foi digitado o número 3.')
print('Os valores pares digitados foram: ', end='')
for n in numb:
    if n % 2 == 0:
        print(n, end=' ')
