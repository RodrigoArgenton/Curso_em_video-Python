# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

validacao = []
userValidacao = str(input('Digite a expressão: '))

for simb in userValidacao:
    if simb == '(':
        validacao.append('(')
    elif simb == ')':
        if len(validacao) > 0:
            validacao.pop()
        else:
            validacao.append(')')
            break
if len(validacao) == 0:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está errada.')