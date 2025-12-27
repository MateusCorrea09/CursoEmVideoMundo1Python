#Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre
# a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário
# se ele quer ou não continuar a digitar valores.
cont_entradas = 1
total_entradas = 0
resposta = 'S'
entrada = int(input('Entre com um número: '))
menor = entrada
maior = entrada
total_entradas += entrada
resposta = str(input('Deseja cotinuar [S / N]? ')).upper()
if resposta == 'S':
    while resposta == 'S':
        entrada = int(input('Entre com um número: '))
        cont_entradas += 1
        total_entradas += entrada
        if entrada > maior:
            maior = entrada
        elif entrada < menor:
            menor = entrada 
        resposta = str(input('Deseja cotinuar [S / N]? ')).upper()
media = total_entradas / cont_entradas
print('A média em relação a todas as entradas é [{}] e o número de entradas totais foram [{}]'.format(media,cont_entradas))
print('O menor número foi [{}]\nE o maior número foi [{}]'.format(menor,maior))