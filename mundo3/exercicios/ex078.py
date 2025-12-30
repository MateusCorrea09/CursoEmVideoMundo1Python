#faça um programa que leia 5 valores numéricos e guarde os em uma lista.
#No final, mostre qual foi o maior e o menor valor digitaso e suas
#  respectivas posições na lista

entradas = []
for indice in range(0,5):
    entradas.append(int(input('entre com um valor: ')))
menor = entradas[0]
posicao_menor = 0
maior =  entradas[0]
posicao_maior = 0
for indice,valor in enumerate(entradas):
    if valor > maior:
        maior = valor
        posicao_maior = indice
    if valor < menor:
        menor = valor
        posicao_menor = indice
print(entradas)
print(f'O maior Número é [{maior}] posição [{posicao_maior}]')
print(f'O menor Número é [{menor}] posição [{posicao_menor}]')