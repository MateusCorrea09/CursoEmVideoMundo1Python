#faça um algoritmo que leia o salário de um funcionário e mostre
#seu novo salário com 15% de AUMENTO!
entrada_salario = float(input('Entre com seu salário atual: R$ '))
desconto = (entrada_salario * 15) / 100
salario_final = entrada_salario + desconto
print('Seu salário com 15% de AUMENTO é de R$[{:.2f}]'.format(salario_final))