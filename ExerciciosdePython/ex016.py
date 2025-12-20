#crie um programa que leia um numero real qualquer
#e mostre na tela a sua porção inteira
import math
entrada = float(input('Entre com um numero real: '))
print('a porção INTEIRA do valor [{}] é [{}]'.format(entrada,math.trunc(entrada)))