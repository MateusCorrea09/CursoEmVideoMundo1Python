#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um
#dos digitos separados.
entrada = input('Entre com um número de 0 a 9999: ')
print('Unidade [{}]'.format(entrada[3]))
print('Dezena [{}]'.format(entrada[2]))
print('Centena [{}]'.format(entrada[1]))
print('Milhar [{}]'.format(entrada[0]))