#um professor quer sortear um dos seus quatro aluno para apagar o quadro
#faça um programa que ajude ele, lendo o nome deles e escrevendo o nome 
#aluno escolhido
import random

#aluno1 = input('Entre com o nome do aluno [1]: ')
#aluno2 = input('Entre com o nome do aluno [2]: ')
#aluno3 = input('Entre com o nome do aluno [3]: ')
#aluno4 = input('Entre com o nome do aluno [4]: ')

#sorteado = random.randint(1,4)
#if(sorteado == 1):
#    print('O aluno sorteado é [{}]'.format(aluno1))
#if(sorteado == 2):
#    print('O aluno sorteado é [{}]'.format(aluno2))
#if(sorteado == 3):
#    print('O aluno sorteado é [{}]'.format(aluno3))
#if(sorteado == 4):
#    print('O aluno sorteado é [{}]'.format(aluno4))

#Resolução do profesor:
n1 = input('Entre com o primeiro aluno: ')
n2 = input('Entre com o segundo aluno: ')
n3 = input('Entre com o terceiro aluno: ')
n4 = input('Entre com o quarto aluno: ')
lista = [n1,n2,n3,n4]
escolhido = random.choice(lista)#só da pra usar o 'choice' através de listas ???? ata ;D
print('O aluno escolhido foi [{}]'.format(lista)) 

