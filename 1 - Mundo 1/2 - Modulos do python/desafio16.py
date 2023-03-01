#Processo abaixo realiza o processo de porção de um valor fracionário através de importação

from math import trunc
num = float(input('Digite um número fracionário: '))
print('O valor digitado foi {:.3f} e a sua porção inteira é {}.'.format(num, trunc(num)))


#Processo abaixo realiza o processo de porção de um valor fracionário através do int

num = float(input('Digite um número fracionário: '))
print('O valor digitado foi {} e a sua porção inteira é {}.'.format(num, int(num)))