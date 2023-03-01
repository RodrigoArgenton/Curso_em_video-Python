from datetime import date
ano = int(input('Que ano deseja analisar se é bissexto?  ou digite 0 para verificar o ano atual que se encontra. '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO.'.format(ano))
else:
    print('O ano {} não é BISSEXTO.' .format(ano))