def leiaint(n):
    while True:
        try:
            m = int(input(n))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número inteiro válido\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mPrograma interrompido pelo usuário\033[m')
            return 0
        else:
            return m

def leiafloat(n):
    while True:
        try:
            m = float(input(n))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número real válido\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mPrograma interrompido pelo usuário\033[m')
            return 0
        else:
            return m