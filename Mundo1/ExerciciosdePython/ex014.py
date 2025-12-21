#Escreva um programa que converta uma temperatura digitada em
#Cº para Fº
entrada_temp = float(input('Entre com a temperatura em Cº: '))
#formula °F=(°C×1,8)+32 (peguei no google :D)
f = (entrada_temp * 1.8) + 32
print('A temperatura de [{}]ºC corresponde a [{}]ºF'.format(entrada_temp,f))