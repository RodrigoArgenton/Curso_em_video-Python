#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

#Variavel para controle da maior idade do sexo masculino
midade = 0
#Varivel para somar as idade e dividir pela quantidade de laços contabilizando a media
somaidade = 0
#variavel para ver a quantidade de mulheres com menos de 20 anos
contidadeF = 0

#Laço de repetição com o objetivo de realizar 3 perguntas e realizar a metrica conforme condicionais
for contnome in range(1,5):
    print("-----{} pessoa-----".format(contnome))
    nome = str(input("Digite o seu primeiro nome: ")) .upper()
    idade = int(input("Digite a sua idade: "))
    sexo = str(input("Digite seu sexo (M para MASCULINO ou F para FEMININO): ")).strip() .upper()
    print("")
    somaidade = idade + somaidade
    if idade > midade and sexo == "M":
        mnome = nome
        midade = idade
    else:
        if sexo == "F" and idade <= 20:
            contidadeF = contidadeF + 1

#Variavel para saber a media de idade dos participantes
media = somaidade / (contnome)


print("")

#Resultado das metricas e informações
print("A média da idade dos participantes é: {}".format(media))
print("A pessoa do sexo masculino com mais idade é o {} com {} anos".format(mnome,midade))
print("Quantidade de mulheres com menos de 20 anos é: {}".format(contidadeF))