#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, 
# crie duas listas extras que vão conter apenas os valores pares e os valores ímpares
# digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista_numerica = []
while True:
    entrada = int(input('Entre com um valor para lista: '))
    lista_numerica.append(entrada)
    resposta = str(input('Deseja continuar[ s / n ]? ')).lower()
    if resposta == 'n':
        break
lista_numerica_par =[]
lista_numerica_impar =[]
for i in lista_numerica:
    if i %2 == 0:
        lista_numerica_par.append(i)
    else:
        lista_numerica_impar.append(i)
print('*'*30)
print(f'A lista completa é: {lista_numerica}')
print('*'*30)
print(f'A lista apenas com pares é {lista_numerica_par}')
print('*'*30)
print(f'A lista apenas com impares é {lista_numerica_impar}')

