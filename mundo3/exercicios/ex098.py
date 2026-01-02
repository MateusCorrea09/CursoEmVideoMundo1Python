# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
#  Seu programa tem que realizar três contagens através da função criada:
#a) de 1 até 10, de 1 em 1
#b) de 10 até 0, de 2 em 2 
#c) uma contagem personalizada

#A minha tentantiva ta até que funcionando, mas sgundo o professor é mais eficiente usar um while ao invés do for nesse exercício
from time import sleep
def contador():
    for i in range(1,11):
        print(f'[{i}] ',end='')
        sleep(0.5)
    print()
    for i in range(10,0,-2):
        print(f'[{i}] ',end='')
        sleep(0.5)
    print()
    inicio = int(input('Entre com o valor do início da contagem: '))
    fim = int(input('Entre com o valor do fim da contagem: '))
    passo = int(input('Entre com o valor do passo da contagem'))
    if passo < 0:
        passo *= -1
    elif passo == 0:
        passo = 1
    if fim < inicio:
        auxi = inicio
        inicio = fim
        fim = auxi
    for i in range(inicio,fim,passo):
        print(f'[{i}] ',end='')
        sleep(0.5)
#contador()

def contador_dois(i, f, p):
    if p < 0:
         p *= -1
    if p == 0:
        p = 1
    print('-='*20)
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ',end='', flush = True)
            sleep(0.5)
            cont+=p
        print('Acabou :D')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ',end='',flush = True)
            sleep(0.5)
            cont -= p
        print('Acabou :D')

contador_dois(7,2,0)