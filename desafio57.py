#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

#Variavel com o objetivo de pegar o sexo do usuário. OBS: nota que após o INPUT, extiste 3 informações importantes, sendo elas: .strip() .upper() [0]. Respectivamente, elas irão retirar os espaços em branco, colocar todas as palavras em maiúsculo e pegar somente a primeira letra localizado no 0.
sexo = str(input('Informe o seu sexo: [M/F] ')).strip() .upper() [0]

#Laço de verificação de dados informado na variavel SEXO
while sexo not in 'MF':
    sexo = str(input('DADO INVALIDO. Por favor, informe o seu sexo: ')).strip() .upper() [0]

#Print de sucesso
print('Sexo {} registrado com sucesso'.format(sexo))