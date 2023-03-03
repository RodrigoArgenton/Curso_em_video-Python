# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

# variavel que recebe o valor a ser analizado
x = input('Digite alguma coisa: ')

# funções de verificação
print(f'O tipo primitivo é? {type(x)}')
print(f'O valor digitado só tem espaços? {x.isspace()}')
print(f'O valor digitado é um número? {x.isnumeric()}')
print(f'O valor digitado é alfabetico? {x.isalpha()}')
print(f'O valor digitado é alfanumerico? {x.isnumeric()}')
print(f'O valor digitado está em maiusculos? {x.isupper()}')
print(f'O valor digitado está minusculo? {x.islower()}')
print(f'O valor digitado está capitalizado? {x.istitle()}')