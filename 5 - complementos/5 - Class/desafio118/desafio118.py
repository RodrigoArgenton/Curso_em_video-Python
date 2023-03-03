# Classe Retangulo: Crie uma classe que modele um retangulo:

# Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
# Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
# Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.
from retangulo import retangulo as rt

# input dos lados do retangulo
x = float(input('Digite a altura do retangulo: '))
y = float(input('Digite o comprimento do retangulo: '))

# set lados do retangulo
retangulo = rt(x, y)
# mostra lados atuais do retangulo
retangulo.mostrarLados()
# set novos lados do retangulo
retangulo.mudarValor(0.5, 0.9)
retangulo.mostrarLados()
# calcular area do retangulo
retangulo.calcularArea()
# calcula perimetro do retangulo
retangulo.calcularPerimetro()
# calcula perimetro do retangulo
retangulo.calcularPisos()

# Acredito que precise ter mais uma funções que calcule um local a ser preenchido pelo piso, uma vez que o perimetro é baseado no valor inserido pelos lados do retangulo, logo, o valor será sempre 2, e foi o que eu realizei, todavia, voltei atras ao verificar que o pessoal que realizou esse exercicio não informou o mesmo no exercicio, mas vou deixar o código comentado a baixo.
# retangulo.calcularPisosV2(10, 20)

# mostra o interactive help da class retangulo
help(retangulo)