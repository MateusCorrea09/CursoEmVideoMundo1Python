# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante
#  ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor 
# numérico. Ex: n = leiaInt(‘Digite um n: ‘)
def leianumero(msg):
    ok = False
    valor = 0
    while True:
        n = str(input('Entre com u número: '))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('Erro! Entre com um número válido!')
        if ok:
            break
    return valor

n = leianumero('Entre com um número: ')
print(f'você acabou de digitar o {n}')