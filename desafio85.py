#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

number = [[], []]

for c in range(1,8):
    userNumber = int(input(f'Digite o {c}° número: '))
    if userNumber % 2 == 0:
        number[0].append(userNumber)
    else:
        number[1].append(userNumber)

print('+'*30)
print(f'Os números pares são {sorted(number[0])}.')
print(f'Os número ímpares são {sorted(number[1])}.')