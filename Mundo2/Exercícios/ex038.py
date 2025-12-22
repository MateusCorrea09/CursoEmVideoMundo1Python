#Escreva um programa que leia dois números inteiros e compare-os, mostrando
#na tela uma mensagem:
#o primeiro valor é o maior
#o segundo valor é o maior
#não existe valor maior, os dois são iguais
n1 = float(input('Entre com o primeiro valor: '))
n2 = float(input('Eentre com o segundo valor: '))

if n1 > n2:
    print('O primeiro valor é maior que o segundo')
elif n2 > n1:
    print('O segundo valor é maior que o primeiro')
elif n1 == n2:
    print('Os valores são iguais!')
else:
    print('Entrada inválida!')