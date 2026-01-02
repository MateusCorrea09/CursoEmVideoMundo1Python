#Faça um programa que tenha uma função chamada maior(),
# que receba vários parâmetros com valores inteiros. Seu programa 
# tem que analisar todos os valores e dizer qual deles é o maior.
'''
Teste :D
numeros = (1,2,9,4,5)
lista_numeros = list()
for i in numeros:
    lista_numeros.append(i)
lista_numeros.sort()
maior = lista_numeros[len(lista_numeros) - 1]
print(maior)
'''
def acha_maior(*num):
    lista_numeros = list()
    for i in num:
        lista_numeros.append([i])
    lista_numeros.sort(reverse= True)
    print(f'O maior número dentre as entradas realizadas é [{lista_numeros[0]}]')

acha_maior(1,2,3,4,5,6)
acha_maior(2,0,3,1,8,11,3,4,5,6,777,7,7,7,9,9)
acha_maior(12,77,54,90,22,67,55,97,84)

#O professor achou uma forma mais eficiênte de chagar no mesmo resultado, no caso não usando listas, quando criamos listas
#nós separamos mais uma parte da memória para guardar informação, então eu acho a solução dele mais otimizada

def chando_o_maior(*num):
    print(f'Os valores de entrada são {num}')
    cont = 0
    maior = 0
    for i in num:
        if cont == 0:
            maior = i
        else:
            if i > maior:
                maior = i
        cont += 1
    print(f'O maior valor é {maior}')
chando_o_maior(1,2,3,4,5,6,7,8)
chando_o_maior(5,6,4,2,7,9,4,21,3,5,6)
chando_o_maior(4,8,6,4,2,8,0,9,6,3,2,5,6,7,8,7,6)
