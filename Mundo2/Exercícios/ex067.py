#faça um programa que mostre a tabuada para cada valor digitado pelo usuário.
# O programa será interrompudo quando o número digitado for negativo!

entrada = int(input('Entre com um número para a tabuada: '))
while True:
    for i in range(1,11):
        print('{} * {} = [{}]'.format(entrada, i, entrada * i))
    print('O loop para quando for digitado um número negativo')
    entrada = int(input('entre com um outro Número: '))
    if entrada < 0:
        break
print('Fim da aplicação!')