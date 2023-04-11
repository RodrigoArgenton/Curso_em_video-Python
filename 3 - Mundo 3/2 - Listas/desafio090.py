# compressão de lista
# desafio que realiza a criação de uma matrix onde a soma de 'x', 'y' e 'z', caso seja igual a 'n' não pode estar na matriz.

listaFor = []
listaCompressao = []

x = int(input())
y = int(input())
z = int(input())
n = int(input())

# ambos comandos realizam o mesmo objetivo, porem, um utiliza o metódo "compressão de lista".
# laço de repetição
for i in range(0, x+1):
    for j in range(0, y+1):
        for z in range(0, z+1):
            if i+j+z != n:
                listaFor.append([i,j,z])
print(listaFor)

# compressão de lista
listaCompressao = [[i,j,k] for i in range(0,x+1) for j in range(0, y+1) for k in range(0, z+1) if i+j+k != n]
print(listaCompressao)