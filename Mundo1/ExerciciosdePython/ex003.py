#crie um programa que elia dois números e mostre
#a soma entre eles
##MINHA RESOLUÇÃO ANTES DE VER O VÍDEO##
n1 = int(input('Entre com N1: '))
n2 = int(input('Entre com N2: '))
resultado = n1 + n2
print(f'A soma de {n1} + {n2} é {resultado}')
##RESOLUÇÃO DO PROFESSOR##
#o professor usou novamente o '.format()' achei interessante 
#isso me lembra como eu fazia em Java, no final colocando em sequencia
#todas as variaveis que vão ser encaixadas durante o print
print('A soma entre {} e {} é igual a {}!'.format(n1,n2,resultado))