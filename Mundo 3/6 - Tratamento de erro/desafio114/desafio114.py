# Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
import urllib
import urllib.request

try:
    site=urllib.request.urlopen('http://www.pudim.com.br/')
except urllib.request.URLError as error:
    print('O site não está acessível no momento', error)
else:
    print('Consegui abrir o site com sucesso!')