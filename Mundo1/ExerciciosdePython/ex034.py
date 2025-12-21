#Escreva um programa que pergunte o sálario de um funcionário e calcule
#o valor do seu aumento!
#Para salários superiores a R$1250,00 calcule um aumento de 10%
#para os inferiopres ou igausl o aumento é de 15%
salario_inicial = float(input('Entre com o seu salário: '))
if salario_inicial > 1250:
    aumento_salarial = (salario_inicial * 10) / 100
    print('O aumento do seu salário é de [{}] e resulta em um salário total de [{}]'.format(aumento_salarial,salario_inicial + aumento_salarial))
else:
    aumento_salarial = (salario_inicial * 15) / 100
    print('O aumento do seu salário é de [{}] e resulta em um salário total de [{}]'.format(aumento_salarial,salario_inicial + aumento_salarial))
 