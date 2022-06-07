frase = str(input('Digite uma frase: ')).lower() .strip()
print('A sua frase têm {} letras.'.format(frase.count('a')))
print('A letra A aparece na posição {}.'.format(frase.find('a')+1))
print('A ulima letra a fica na posição {}.'.format(frase.rfind('a')+1))