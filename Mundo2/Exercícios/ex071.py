#Crie um programa que funcione como um caiza eletrônico. No inicío, pergunte ao
#usuário qual será o valor a ser sacada (número inteiro) e o programa vai informar
#quantas cédulas de cada valores serão entregues.

valor = int(input('Entre com o valor que deseja ser sacado: '))
while True:
    print('[{}] notas de R$50'.format(valor//50))
    valor = valor % 50
    print('[{}] notas de R$20'.format(valor//20))
    valor = valor % 20
    print('[{}] notas de R$10'.format(valor//10))
    valor = valor % 10
    print('[{}] notas de R$1'.format(valor//1))
    valor = valor % 1
    if valor == 0:
       break
print(valor)
print('fim do programa')