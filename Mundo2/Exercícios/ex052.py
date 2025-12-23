#faça um programa que leia um número inteiro e diga se ele é ou não um número primo
#fiquei um poco na dúvida de como criar um algoritmo que fizesse a checagem se o número é primo ou não
#então pensei nesse código abaixo:
entrada = int(input('Entre com um número: '))
contador_divisoes = 0
for i in range(1,entrada + 1):
    if entrada % i == 0:
        contador_divisoes = contador_divisoes + 1
        if contador_divisoes > 2:
            print('Esse número não é primo!')
            break #Acho que esse é o recurso mais a frente que eu usei, o professor não falou sobre ele ainda... mas ele se encaixa perfeitamente aki
if contador_divisoes <=2:
    print('[{}] esse número é primo'.format(entrada))

#Soluçaõ do professor:
total_divi = 0
print('\nSolução do professor:')
for c in range(1,entrada + 1):
    if entrada % c == 0:
        print('\033[33m',end='')
        total_divi = total_divi + 1
    else:
        print('\033[31m',end='')
    print('{} '.format(c),end='')
print('\nO total de divisores é [{}]'.format(total_divi))
