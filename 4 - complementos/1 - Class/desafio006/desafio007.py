def reverse_words_order_and_swap_cases(sentence):
    lista = []
    for letra in  sentence:
        if letra.islower():
            lista.append(letra.upper())
        elif letra.isupper():
            lista.append(letra.lower())
        else:
            lista.append(letra)
    
    lista = ''.join(lista)
    lista = lista.split()
    lista = lista[::-1]
    return ' '.join(lista)

user = str(input('Digite uma frase: '))
print(reverse_words_order_and_swap_cases(user))