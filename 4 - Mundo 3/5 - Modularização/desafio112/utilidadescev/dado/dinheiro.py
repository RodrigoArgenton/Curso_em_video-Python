def leiadinheiro(msg):
    while True:
        respota = str(input(msg)) .strip() .replace(',', '.')
        if respota.isalpha() or respota == '':
            print('\033[0;31mValor inserido é invalido!\033[m')
        else:
            return float(respota)