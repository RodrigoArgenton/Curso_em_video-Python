def metade(d, forma=False):
    result = d/2
    return result if forma is False else moeda(result)

def dobro(d, forma=False):
    result = d *2
    return result if forma is False else moeda(result)

def diminuir(d, t=10, forma=False):
    result = d - (d * (t/100))
    return result if forma is False else moeda(result)

def aumentar(d, t=10, forma=False):
    result = d + (d * (t/100))
    return result if forma is False else moeda(result)

def moeda(moeda = 0, m = 'R$', forma=False):
    return f'{m} {moeda:.2f}'.replace('.',',')

def resumo(valor, aumento, diminui):
    print('-'*50)
    print(f"{'RESUMO DO VALOR':^50}")
    print('-'*50)
    print(f'Preço analisado: \t\t\t{moeda(valor)}')
    print(f'Dobro do preço: \t\t\t{dobro(valor, True)}')
    print(f'Metade do preço: \t\t\t{metade(valor, True)}')
    print(f'{aumento}% de aumento: \t\t\t\t{aumentar(valor, aumento, True)}')
    print(f'{diminui}% de redução: \t\t\t{diminuir(valor, diminui, True)}')
    print('-'*50)