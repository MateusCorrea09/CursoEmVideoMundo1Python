#faça um programa que leia um número qualquer e mostre o seu fatorial.
#5! = 5x4x3x2x1 = 120
resp = 0
entrada = int(input('Entre co um número: '))
cont = entrada - 1
while cont != 0:
    if cont == entrada - 1:
        fatorial = entrada * cont
        resp = resp + fatorial
    else:
        fatorial = cont * resp 
        resp = fatorial
    cont = cont - 1
print(resp)