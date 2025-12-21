#Desenvovla um programa que leia o comprimento de três retas e diga ao 
#usuário se elas podem ou não formar um tinângulo
# cada uma das entradas deve ser menor que a soma das outras duas entradas para formar um triangulo

n1 = float(input('Entre com a primeira medida: '))
n2 = float(input('Entre com a segunda medida: '))
n3 = float(input('Entre com a terceira medida: '))

#Cada entrada deve ser menor que a soma das outras duas entradas...
if n1 < n2 + n3:
    if n2 < n1 + n3:
        if n3 < n1 + n2:
            print('🔺É possível fazer um triângulo!🔺')
        else:
            print('Não é possível fazer um triângulo!')
    else:
        print('Não é possível fazer um triângulo!')
elif n2 < n1 + n3:
    if n1 < n2 + n3:
        if n3 < n1 + n2:
            print('🔺é possível fazer um triângulo!🔺')
        else:
            print('Não é possível fazer um triângulo!')
    else:
        print('Não é possível fazer um triângulo!')
elif n3 < n1 + n2:
    if n1 < n2 + n3:
        if n2 < n1 + n3:
            print('🔺É possível fazer um triângulo!🔺')
        else:
            print('Não é possível fazer um triângulo!')
    else:
        print('Não é possível fazer um triângulo!')