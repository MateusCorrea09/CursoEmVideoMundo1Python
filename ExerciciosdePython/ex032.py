#faça um programa que leia um ano qualquer e mostre se ele é bissexto

entrada = int(input('Entre com um ano: '))
if entrada % 4 == 0:
    print('O ano é bissexto!')
elif entrada % 100 != 0:
    print('O ano não é bissexto!')
elif entrada % 400 == 0:
    print('Ano bissexto!')
else:
    print('Erro')