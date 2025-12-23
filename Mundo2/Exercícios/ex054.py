#Crie um programa que leia o ano de nascimento de sete pessoas
#no final, mostre quantas pessoas ainda não atingiram a maioridade
#e quantas já são maiores de idade
from datetime import date
menor_idade = 0
maior_idade = 0
ano_atual = date.today().year
for i in range(0,7):
    entrada = int(input('Entre com seu ano de nascimento: '))
    if ano_atual - entrada < 18:
        menor_idade = menor_idade + 1
        #print(entrada - ano_atual)
    else:
        maior_idade = maior_idade + 1
        #print(entrada - ano_atual)
print('O número de pessoas na maior idade é de [{}]\nO número de pessoas na menor idade é de [{}]'.format(maior_idade, menor_idade))
