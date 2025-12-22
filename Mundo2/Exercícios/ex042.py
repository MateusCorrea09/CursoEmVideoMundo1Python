#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#EQUILÁTERO: todos os lados iguais ISÓSCELES: dois lados iguais, um diferente ou ESCALENO: todos os lados diferentes
n1 = int(input('Entre com o Primeiro Número: '))
n2 = int(input('Entre com o Segundo Número: '))
n3 = int(input('Entre com o Terceiro Número: '))
#verificação de possibilidade de formar um triângulo:

if n1 < n2 + n3 and n2 < n1 + n2 and n3 < n1 + n2:
    print('Forma um triângulo!')
    if n1 == n2 == n3:
        print('EQUILÁTERO')
    elif n1 != n2 != n3:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Não é possível formar um triângulo!')
