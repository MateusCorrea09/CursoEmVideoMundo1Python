#Faça um programa que leia o nome completo de uma pessoa
#mostrando em seguida o primeiro e o último nome separadamente.

nome = input('Entre com seu nome: ')
lista_nome = nome.split()
print('O seu primeiro nome é [{}]'.format(lista_nome[0]))
print('O seu último nome é [{}]'.format(lista_nome[len(lista_nome) - 1]))