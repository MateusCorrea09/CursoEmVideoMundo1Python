#Excreva um programa para aprovar o empréstimo brancário para a compra
#de uma casa. O programa vai perguntar o valor da casa, o salário do comprador
# e em quantos anos ele vai pagar
# CALCULE O VALOR DA PRESTAÇÃO MENSAL, SABENDO QUE ELA NÃO PODE EXCEDER 30# DO
# #SALÁRIO OU ENTÃO O EMPRÉSTIMO SERÁ NEGADO
# tenho que pagar o valor da casa  dividir pelo nº de anos... ai eu acho o valor das prestações
# essas mesmas prestações devem ser contidas em um valor igual a 30º do salário do cliente
# se exceder o empréstimo deve ser negado 
salario = float(input('Entre co seu salário?: '))
valor_casa = float(input('Entre com o valor da casa: '))
anos_prestacao = int(input('Entre com o nº de ANOS de empréstimos solicitados: '))# cada ano tem 12 meses
#calculo eu tenho que pegar o valor total da casa e dividir pelo numero de meses, apra encontrar o valor a ser pago por cada mês
prestacao_final = valor_casa / (anos_prestacao * 12)
#eu preciso encontrar o valor correspondente a 30% do salário do cliente, para saber se é possível liberar o empréstimo
salario_analise = salario * 30 / 100

if prestacao_final <= salario_analise:
    print('\033[4;34mempréstimo aceito!\033[32m')
    print('A prestação será de [\033[4;34mR$ {:.2f}\033[32m] por [\033[4;34m{}\033[32m] anos'.format(prestacao_final,anos_prestacao))
else:
    print('Empréstimo negado!')