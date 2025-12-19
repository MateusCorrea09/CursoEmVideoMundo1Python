#faça um programa que leia algo pelo teclado e mostre na tela 
#seu tipo primitivo e todas as informações possíveis sobre ela.
n = input('entre com um numero: ')
print('O tipo da entrada é [{}]'.format(type(n)))
print('só tem espaço? [{}]'.format(n.isspace()))
print('é um número? [{}]'.format(n.isnumeric()))
print('é um alfabético [{}]'.format(n.isalpha))
print('é alfabumerico? [{}]'.format(n.isalnum())) #alfanumerico numero + letra
print('está em  maiúsculo? [{}]'.format(n.isupper))
print('está em minusculo? [{}]'.format(n.islower))
print('está em capitalizada? [{}]'.format(n.istitle))