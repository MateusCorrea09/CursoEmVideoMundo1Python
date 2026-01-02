#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
#  A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai 
#  mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint
def sortea_numero():
    lista_numeros = list()
    lista_numeros.append(randint(0,60))
    lista_numeros.append(randint(0,60))
    lista_numeros.append(randint(0,60))
    lista_numeros.append(randint(0,60))
    lista_numeros.append(randint(0,60))
    lista_numeros.append(randint(0,60))
    return lista_numeros

def soma_pares(numeros):
    total = 0
    for i in numeros:
        if i % 2 ==0:
            total += i
    return total

def Resultado():
    numeros = sortea_numero()
    print(f'os numeros sorteados foram {numeros}')
    ponto = soma_pares(numeros)
    print(f'A soma dos números pares é {ponto}')

Resultado()
    
