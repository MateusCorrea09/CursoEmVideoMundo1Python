#o msmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos
#faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random
n1 = input('Entre com o primeiro aluno: ')
n2 = input('Entre com o segundo aluno: ')
n3 = input('Entre com o terceiro aluno: ')
n4 = input('Entre com o quarto aluno: ')
lista = [n1,n2,n3,n4]
escolhido = random.choice(lista)
print('O primeiro aluno a apresentar o trabalho é [{}]'.format(escolhido))