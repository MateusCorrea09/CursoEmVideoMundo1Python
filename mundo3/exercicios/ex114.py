#Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except Exception as erro:
    print(f'Deu erro! {erro}')
else:
    print('Está tudo ok!')