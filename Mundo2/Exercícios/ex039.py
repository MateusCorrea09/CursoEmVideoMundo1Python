#Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
#  se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do
#  alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
ano_atual = int(input('Entre com o ano atual: '))
data_nascimento = int(input('Entre com sua data de nascimento: '))
idade = ano_atual - data_nascimento
print(idade)
if idade > 18:
    print('Você passou do tempo de alistamento! um atrazo de [{}]'.format(idade - 18))
elif idade == 18:
    print('Vcoê deve se alistar neste ano! pois é a idade atual')
else:
    print('Você não está na hora de se alistar ainda! você ainda tem [{}]'.format(idade))

#resolução do professor mostrou uma funcionalidade do python de identificar o ano atual com base na informação
#disponibilizada pelo computador ...  que seria o 'atual = date.today().year' achei legal
 