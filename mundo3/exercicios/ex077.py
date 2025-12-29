#Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
palavras = ('abacate','limao','laranga','jabuticaba','melao')
for palavra in palavras:
    for letra in palavra:
        if letra in 'aeiou':
            print(f'Na palavra {palavra} temos {letra}')
#empaquei, não consegui achar um jeito de printar a palavra apenas uma unica vez :D
for palavra in palavras:
    print(f'\nNa plavra {palavra} temos ',end='') #O professor dividiu os primts, e os organizou com o 'end',
                                                    #o meu erro foi pensar que deveria ser colocado em um unico print
    for letra in palavra:
        if letra in 'aeiou':
            print(f' {letra}',end=' ')