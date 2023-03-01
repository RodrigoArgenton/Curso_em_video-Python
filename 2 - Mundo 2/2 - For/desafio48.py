#Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.



v = int(input("Digite um valor para saber a quantidade de números ímpares e a soma dos mesmos: "))

#Declaração de variáveis de contagens de numéros ímpares (cont) e soma (soma) que é a soma de todos os números ímpares
cont = 0
soma = 0
v = v + 1
#Laço que tém como objetivo, "mostrar" todos os número entre 1 e 500 pulando em 2
for n in range(1, v, 2):
#Condicional que verifica se o valor informado acima é divisivel por 3
    if n % 3 == 0:
        cont = cont + 1
        soma = soma + n
        print(n, end=(" "))
print("")
print(50*"-")
print("A quantidade de números ímpares do 1 até o {} é {}.".format(v-1, cont))
print("A soma dos números ímpares do 1 até o {} é {}.".format(v-1, soma))
print(50*"-")