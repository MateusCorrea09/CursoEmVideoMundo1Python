#Faça um programa que leia o comprimento da cateto oposto e do cateto adjacente de um trinângulo retângulo
#calcule e moostre o comprimento da hipotenusa.
#o quadrado da hipotenusa é a soma dos quadrados dos catetos
import math
entrada = float(input('Entre com o cateto OPOSTO: '))
entrada2 = float(input('Entre com o cateto ADJACENTE: '))
hipotenuza = math.pow(entrada,2) + math.pow(entrada2,2)
print('A hipotenuza é igual a [{:.2f}]'.format(math.sqrt(hipotenuza)))