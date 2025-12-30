#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.

lista_numerica = []
cinco = False
while True:
    entrada = int(input('Entre com um valor: '))
    if entrada == 5:
        cinco = True
    lista_numerica.append(entrada)
    resp = str(input('Deseja continuar [s/n]? ')).lower()
    if resp == 'n':
        break
lista_numerica.sort(reverse=True)
print(lista_numerica)
print(f'A lista possuí {len(lista_numerica)} itens')
if cinco == True:
    print('O cinco foi digitado!')
else:
    print('O cinco não foi digitado!')