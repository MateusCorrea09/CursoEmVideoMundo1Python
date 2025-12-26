#Faça o deafio 051, dendo o primeiiro termo e a razão de uma pa, mostrando
#os 10 primerios termos da progressão usando a estrutura while
 #   conteudo = entrada + (i - 1) * entrada_razao
n1 = int(input('Entre com um número: '))
razao = int(input('Entre com a razao: '))
cont = 0
conteudo = 0
while cont != 10:
    conteudo = n1 + (cont + 1) * razao
    cont = cont + 1
    print(cont,conteudo)