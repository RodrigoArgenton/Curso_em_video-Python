lista = []

N = int(input())
for i in range(N):
    valor = str(input()) .split()

    for i in valor:
        if len(valor) >= 2:
            valor[1] = int(valor[1])
            if len(valor) == 3:
                valor[2] = int(valor[2])
    
    if valor[0] == 'insert':
        lista.insert(int(valor[1]), int(valor[2]))
    elif valor[0] == 'print':
        print(lista)
    elif valor[0] == 'remove':
        lista.remove(int(valor[1]))
    elif valor[0] == 'append':
        lista.append(valor[1])
    elif valor[0] == 'sort':
        lista.sort()
    elif valor[0] == 'pop':
        lista.pop()
    elif valor[0] == 'reverse':
        lista.reverse()
    print(valor)
    valor.clear()