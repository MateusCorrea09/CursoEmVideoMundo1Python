
def ajuda(str):
    help(str)
def titulo(msg,cor=0):
    tam = len(msg)
    print('~' * tam)
    print(msg)
    print('~' * tam)
comando = ''
while True:
    titulo('Sistema de ajuda pyHelp')
    comando = str(input('Entre com uma função ou biblioteca que deseja saber mais: '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('Até logo')