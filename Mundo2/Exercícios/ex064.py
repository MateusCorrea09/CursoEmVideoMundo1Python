#Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado.
#  O programa só vai parar quando o usuário digitar o valor 999, que é a condição de 
# parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles
#  (desconsiderando o flag).
entrada = None
conta_entradas = 0
soma_entradas = 0
while entrada != 999:
    print('A condição de parada é a entrada ser "999"! ')
    entrada = int(input('Entre com um número:'))
    if entrada != 999:
        conta_entradas += 1
        soma_entradas += entrada
print('O total de entradas é [{}]\nA Soma de todas as entradas é [{}]'.format(conta_entradas,soma_entradas))