#Crie um programa que tenha uma tupla totalmen te preenchida com uma
#contagem por extensão, de zero até vinte.
# seu programa deverá ler um número pelo teclado (entr 0 e 20) e mostrá-lo por extensão

numeros = ('zero','um', 'dois','três','Quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezessis','dezesete','dezoito','dezenove','vinte')
while True:
    entrada = int(input('Entre com um número entre 0 - 20 : '))
    if entrada > 20 or entrada < 0:
        print('Entre com um número válido!')
    if 0 <= entrada <= 20:
        print(numeros[entrada])
        break