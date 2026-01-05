#Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
#  o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a 
# ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
def ficha(nome = '<desconhecido>', gols = 0):
    print(f'O jogador {nome} fez {gols} gols no campeonato')

nome = str(input('Entre com o nome do jogador: '))
gols = str(input(f'Entre com o número de gols que {nome} fez: '))
if gols.isnumeric(): # se essa string for possível ser um número será convertida para inteiro
    gols = int(gols)
else: #se não (isso significa "ABc" ou "3.75") essa mesma se tornará '0'
    gols = 0
if nome.strip() == '': #Faz a verificação se o argumento 'nome' está vazio
    ficha(gols=gols)
else:
    ficha(nome,gols)

#ficha(nome,gols)