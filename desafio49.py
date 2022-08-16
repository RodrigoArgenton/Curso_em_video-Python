#Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for

#Variaveis com o bjetivo de captar informações que o usuário deseja, nesse exemplo, será o valor da tabuada e a quantidade de vezes que a mesma será multiplicada.
tabu = int(input("Digite o valor para saber a tabuada do mesmo: "))
multi = int(input("Digite o multiplicador maximo dessa tabuada: "))

#Laço com o objetivo de realizar a tabuada
for c in range (1, multi + 1):
    print("{} X {} : {}".format(c, tabu, c * tabu))