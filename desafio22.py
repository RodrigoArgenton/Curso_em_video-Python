# programa com o objetido de receber um nome e realizar uma sere de fatores como: deixar maiúsculo e minutos,
# informar a quantidade de letras no total e informar a quantidade de letras no primeiro nome ler o nome do usuário

# .strip (retirar os espaços Right e left do nome)
nome = str(input('Digite o seu nome completo: ')).strip()

print('Aguarde um instante...')

# tranformar o nome em maiusculo e minusculo
print('Seu nome maiúscilo é: {}'.format(nome.upper()))
print('seu nome minusculo é: {}'.format(nome.lower()))

# emitir quantidade de caracteres
print('A quantidade de letras que o seu nome têm é: {}'.format(len(nome) - nome.count(' ')))

# emitir a quatidade de letras no primeiro nome
# print('Seu primeiro nome têm {} letras'.format(nome.find(' ')))

# emitir o primeiro nome e a quantidade de letras (o processo é realizado de forma diferente para entender melhor.
separa = nome.split()
print('Seu nome é {} e têm {} letras.'.format(separa[0], len(separa[0])))
