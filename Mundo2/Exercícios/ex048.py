#faça um programa que calcule a soma entre todos os números ímpares que
#que são multiplos de trÊs e que se encontram no intervalo de 1 a 500
#Teste para verificar uma ideia
#entrada = 3
#multiplo = 102
#if multiplo % 3 == 0:
#    print('Restou zero')
#else:
#    print('NÃO restou zero')
contador = 0
soma_total = 0
for i in range(1,500):
    if i % 2 != 0: #checagem se é ímpar... se não
        if i % 3 == 0:#verifica se é multiplo de 3
            contador = contador + 1
            soma_total =soma_total + i
print('O número de multiplos de 3 no intervalo de 1 a 500 é de [{}]\n A soma total de todos os números é de [{}]'.format(contador,soma_total))