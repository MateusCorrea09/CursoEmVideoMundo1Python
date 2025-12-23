#desenvolva um programa que leia seis números inteiros e mostre
#a soma apenas daqueles que forem pares. Se o valor digitado for
#ímpar desconsidere-o
soma_total = 0
for i in range(0,6):
    entrada = int(input('Entre com um valor inteiro: '))
    if entrada % 2 == 0:
        soma_total = soma_total + entrada
print('A soma de todos os pares é [{}]'.format(soma_total))