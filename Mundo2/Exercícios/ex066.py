#Crie um programa que leia vários n´meros interios pelo teclado. O programa
#só vai parar quando o usuário digitar '999', que é a condição de parada.
# No final mostre quantos números foram digitados e qual foi a soma entre eles.
# desconsideranmdo a flag

cont_entradas = soma_entradas = 0
while True:
    entrada = int(input('Entre com um número: '))
    if entrada == 999:
        break
    cont_entradas += 1
    soma_entradas += entrada
print('O total de entradas é [{}]\nE a soma entre todas elas é [{}]'.format(cont_entradas,soma_entradas))