#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.


print(20*"==")
print("OS 10 PRIMEIROS TERMOS DE UMA PA")
print(20*"==")

#Variaveis com o bjetivo de receber o termo e a razão para realizar uma PA (progressão aritmetica)
ptermo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a Razão: "))

#(ptermo) O ptermo entrou como o primeiro número que será mostrado no laço e como start para realizar a PA
#(razao - razao * 10) A razão seria o valor que será somado ao valor anterior e o valor que será multiplicado para ver o DECIMO termo dessa PA, por conta do mesmo, se encontra multiplicado por 10
for c in range(ptermo, razao * 10, razao):
    print("{} - ".format(ptermo), end=(""))
    ptermo = razao + ptermo
print("Acabou")