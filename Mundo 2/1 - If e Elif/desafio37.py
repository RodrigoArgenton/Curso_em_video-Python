#software que tranforma valores em binário, octal e hexadecial
num = int(input('Digite um número: '))
print('''Digite a opção: 
    [ 1 ] Converter para binário
    [ 2 ] Converter para octal
    [ 3 ] Converter para hexadecimal''')
opcao = int(input('Digite a opção: '))

#condicionais
#[2:] remete a quantos caracteres vai pular do valor informado no bin, oct e hex, ou seja será pulado dois caracter, mas não tem regra para ignorar no final.
if opcao == 1:
    print('O número inserido {} ficaria {} em binário.'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('o número inserido {} ficaria {} em octal.'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('o número inserido {} ficaria {} em hexadecimal.'.format(num, hex(num)[2:]))
else:
    print('Valor inserido invalido')
