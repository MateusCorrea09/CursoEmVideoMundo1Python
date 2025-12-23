#faça um programa que leia o peso de cinco pessoas. No final mostre qual
#foi o mmaior e o menor peso lidos.
maior_peso = 0
menor_peso = 0
entrada = float(input('Entre com sue peso em KG: '))
maior_peso = entrada
menor_peso = entrada
for i in range(0,4):
    entrada_loop = float(input('Entre com sue peso em KG: '))
    if entrada_loop > maior_peso:
        maior_peso = entrada
    elif entrada_loop < menor_peso:
        menor_peso = entrada_loop
print('O maior peso foi [{}]'.format(maior_peso))
print('O menor peso foi [{}]'.format(menor_peso))