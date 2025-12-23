#Desenvolva um programa que leia o nome, idade, sexo de 4 pessoas. No final
#mostre:
#A média de idade do grupo.
#Qual é o nome do homem mais velho.
#Quantas mulheres tem menos de 20 anos.
media_idade_geral = 0
nome_idoso = ''
idade_idoso = 0
cont_idade_mulheres = 0

for i in range(0, 4):
    nome = str(input('Entre com seu nome:\n '))
    sexo = int(input('Entre com seu gênero: \n 1 - Mulher\n 2 - Homem \n 3 - Prefiro não dizer\n'))
    idade = int(input('Entre com sua idade:\n '))

    media_idade_geral = media_idade_geral + idade
    if sexo == 1 and idade < 20:
        cont_idade_mulheres = cont_idade_mulheres + 1
    elif sexo == 2:
        if idade > idade_idoso:
            idade_idoso = idade
            nome_idoso = nome
print('A média de idade geral é [{}]'.format(media_idade_geral // 4))
print('O número de mulheres com menos de 20 anos é [{}]'.format(cont_idade_mulheres))
print('A idade do homem mais velho é [{}] e seu nome é [{}]'.format(idade_idoso,nome_idoso))
    