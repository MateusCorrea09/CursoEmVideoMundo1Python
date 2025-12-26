#Crie um programa que leia dois valores e mostre um menu na tela:
#1 = somar, 2 = multiplicar, 3 = maior, 4 = novos números, 5 = sair do programa
n1 = int(input('Entre com um valor: '))
n2 = int(input('Entre com outro valor: '))
r = 0
while r != 5:
    print('Você entrou com [{}] e [{}]'.format(n1,n2))
    r = int(input('Oa que deseja fazer?\n[1] soma\n[2] multiplicar\n[3] descobrir qual é o maior\n[4] entrar com novos valores\n[5] sair do programa'))
    if r == 1:
        resp = n1 + n2
        print('A soma de [{}] e [{}] é igual a [{}]'.format(n1,n2,resp))
    elif r == 2:
        resp = n1 * n2
        print('A multiplicação de [{}] por [{}] é igual a [{}]'.format(n1,n2,resp))
    elif r == 3:
        if n1 > n2:
            print('O maior valor dentre as duas entradas é [{}]'.format(n1))
        elif n2 > n1:
            print('O maior valor dentre as entradas é [{}]'.format(n2))
        elif n1 == n2:
            print('Ambos os valores são iguais! [{}] e [{}]'.format(n1,n2))
    elif r == 4:
        n1 = int(input('Entre com o valor de n1: '))
        n2 = int(input('Entre com o valor de n2: '))
        print('Os valores foram atualizados! \nn1 = [{}] e n2 = [{}]'.format(n1,n2))
print('Você saiu do programa! até mais tarde :D')