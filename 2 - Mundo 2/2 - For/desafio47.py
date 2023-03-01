from time import sleep

#Esse laço tem como objetivo mostrar somente os números pares entre 1 e 50, todavia, o mesmo realiza esforço desnecessário onde realiza dois laços para mostrar um valor.
'''for c in range (1, 51):
    print('.')
    if c % 2 == 0:
        sleep(1)
        print(c)'''

#desta forma, o programa realiza somente um laço para mostrar cada resultado
'''for c in range (2, 51, 2):
    print('.')
    print(c)
    sleep(1)'''

# Coloquei uma váriavel com o objetivo de ser mais dinâmico
vf = int(input('Digite um valor: '))

for vf in range (2, vf + 1, 2):
    print('.')
    print(vf)
    sleep(1)
