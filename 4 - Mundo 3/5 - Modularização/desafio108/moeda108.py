def metade(d):
    result = d/2
    return result

def dobro(d):
    result = d *2
    return result

def diminuir(d, t=10):
    result = d - (d * (t/100))
    return result

def aumentar(d, t=10):
    result = d + (d * (t/100))
    return result

def moeda(moeda = 0, m = 'R$'):
    return f'{m} {moeda:.2f}'.replace('.',',')