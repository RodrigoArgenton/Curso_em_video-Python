#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

lista = []

for c in range (0,5):
    userNumber = int(input('Digite um número: '))
    if c == 0 or userNumber > lista[-1]:
        lista.append(userNumber)
        print('O número foi adicionado ao final da lista!')
    else:
        cont = 0
        while cont < len(lista):
            if userNumber <= lista[cont]:
                lista.insert(cont, userNumber)
                print(f'O número foi adicionado na posição: {cont}')
                break
            cont += 1

print(lista)