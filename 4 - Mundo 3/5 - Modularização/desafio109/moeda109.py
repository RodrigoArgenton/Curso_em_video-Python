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