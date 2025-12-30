#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
#  Caso o número já exista
cont = 0
lista_numerica = []
while True:
    entrada = int(input('Entre com um valor: '))
    if entrada in lista_numerica:
        print('Valor duplicado')
    else:    
        lista_numerica.append(entrada)
    resposta = str(input('Deseja continuar? [s/n]')).lower()
    if resposta == 'n':
        break
#print(lista_numerica)
lista_numerica.sort()
print(lista_numerica)