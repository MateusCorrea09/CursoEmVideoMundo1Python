#Escreva um programa que pergunte a quantidade de Km percorrido por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a ser pago 
#pelo aluguel sabendo que o carro custa R$60 por dia e R$0,15 por KM rodado
entrada_dias = int(input('Entre com o total de dias em que o carro foi alugado: '))
entrada_km = float(input('Entre com o total de KM rodado: '))
valor_do_aluguel = (entrada_dias * 60)+(entrada_km * 0.15)
print('O valor a ser pago é de R$[{:.2f}]'.format(valor_do_aluguel))