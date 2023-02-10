# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
# Quantidade de notas 
# A maior nota 
# A menor nota 
# A média da turma  
# A situação (opcional)


def nota(num, sit=False):

    listaNota = {}
    maiorNota = 0
    menorNota = 0
    for c in range(0, len(num)):
        if c == 0:
            maiorNota = num[c]
        elif num[c] > maiorNota:
            maiorNota = num[c]
        if c == 0:
            menorNota = num[c]
        elif num[c] < menorNota:
            menorNota = num[c]
    
    media = sum(num) / len(num)

    listaNota = {'Quantidade de notas':len(num), 'Maior Nota': maiorNota, 'Menor Nota': menorNota, 'Média': media}
    
    if sit == True:
        if media >= 7:
            status = 'Bom'
        elif media >= 6:
            status = 'Regular'
        elif media < 6:
            status = 'Ruim'
        listaNota['Status'] = status
    
    return listaNota

respUser = []

while True:
    userResp = int(input('Digite a nota: '))
    respUser.append(userResp)
    cont = str(input('Deseja continuar? [S/N] ')) .upper() .strip() [0]
    
    if cont in 'N':
        break

sitUSer = str(input('Deseja mostrar a situação da nota? [S/N]')).upper() .strip() [0]

if sitUSer in 'S':
    sitUSer = True
else:
    sitUSer = False

resp = nota(respUser, sitUSer)
print(resp)