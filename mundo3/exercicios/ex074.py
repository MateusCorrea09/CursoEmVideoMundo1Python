#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla
#depois disso, mostre a listagem de números gerados e também indique o menor e o maior
# valor que estão na tupla

import random
a = random.randint(-999,999)
b = random.randint(-999,999)
c = random.randint(-999,999)
d = random.randint(-999,999)
d = random.randint(-999,999)
tupla = (a,b,c,d)
print(f'A tupla é composta por : {tupla}')
menor = a
maior = a
for i in tupla:
    if i < menor:
        menor = i
    if i > maior:
        maior = i
print(f'O maior número dentro da tupla é [{maior}]\nE o menor é [{menor}]')
# O professor usou uma outra solução mais eficiênte para esse exercícios
print('Solução do professor:')
n = (random.randint(1,9),random.randint(1,9),random.randint(1,9),random.randint(1,9),random.randint(1,9))
#Dessa forma são colcoados 5 itens aleatórios dentro da tupla
print(n)