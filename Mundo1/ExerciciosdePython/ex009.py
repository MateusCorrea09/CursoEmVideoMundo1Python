#Exercício Python 9: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.
entrada = int(input('entre com um número a ser calculado na tabuada: '))
for i in range(11):
    print('{} * {} = [{}]'.format(i,entrada,entrada * i))