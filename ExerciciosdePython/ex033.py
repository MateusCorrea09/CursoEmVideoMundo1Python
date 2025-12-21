#Faça um programa que elia três números e mostre qual é o maior e qual
#é o menor
n1 = float(input('Entre com o primeiro número: '))
n2 = float(input('Entre com o segundo número: '))
n3 = float(input('Entre com o terceiro Número: '))
#Nesse eu queria fazer algo só usando as coisas que foram ensinadas na aula, ele só não falolu do 'Elif' mas tentei fazer
#de uma forma mais longa como se fosse a primeira vez que eu eu tivesse vendo esse assunto... em outra situação eu usaria um loop de 'for' :D
if n1 > n2:
    if n1 > n3:
        print('o primeiro número [{}] é o maior'.format(n1))
        if n2 > n3:
            print('O terceiro número [{}] é o menor'.format(n3))
        else:
            print('O segundo número [{}] é o menor'.format(n2))
    else:
        print('O terceiro número [{}] é o Maior'.format(n3))
        print('O segundo número [{}] é o Menor'.format(n2))
elif n2 > n1:
    if n2 > n3:
        print('O segundo número [{}] é o maior'.format(n2))
        if n3 > n1:
            print('O primriro é o número é o menor [{}]'.format(n1))
        else:
            print('O terceiro número é o menor [{}]'.format(n3))
    else:
        print('O terceiro número [{}] é o Maior'.format(n3))
        print('O primeiro número [{}] é o Menor'.format(n1))
elif n3 > n1:
    if n3 > n2:
        print('O terceiro número [{}]é o Maior'.format(n3))
        if n2 > n1:
            print('O primeiro número [{}] é o Menor'.format(n1))
        else:
            print('O segundo número [{}] é o Menor'.format(n2))
    else:
        print('O segundo número [{}] é o Maior'.format(n2))
        print('O peimrito número [{}] é o menor'.format(n1))
else:
    print('Erro!')