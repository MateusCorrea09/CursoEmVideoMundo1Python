#desenvolva um programa que leia seis números inteiros e mostre
#a soma apenas daqueles que forem pares. Se o valor digitado for
#ímpar desconsidere-o
soma_total = 0
cont_par = 0
for i in range(0,6):
    entrada = int(input('Entre com um valor inteiro: '))
    if entrada % 2 == 0:
        soma_total = soma_total + entrada
        cont_par = cont_par + 1
print('A soma de todos os pares é [{}]\n E você informou [{}] números pares'.format(soma_total,cont_par))