#Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento
#  de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL 
# e OBRIGATÓRIO nas eleições.
import datetime
#ano = datetime.date.today().year
#print(ano)
#help(datetime) #usei esse aki pra lembrar como usa o datetime
def voto(data):
    ano = datetime.date.today().year
    resultado = ano - data
    if 18 > resultado >= 16:
        return 'Opcional'
    elif resultado >= 18:
        return 'Obrigatório'
    else:
        return 'Negado'
entrada = int(input('Entre com sua data de nascimento: '))
print(voto(entrada))


