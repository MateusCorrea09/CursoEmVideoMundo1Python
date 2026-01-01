#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados
#  em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou
#  o maior número no dado

"""
Esse era um teste que eu tava fazendo, queria tentar ver se o sort() funcionava para ordenar a lista de dicionarios
não deu certo... vou ver a aula para entender como resolver
jogada1 = {'jogador4': 2}
jogada2 = {'jogador3': 1,}
jogada3 ={'jogador2': 4}
jogada4 = {'jogador1': 1,}
jogada = list()
jogada.append(jogada1.copy())
jogada.append(jogada2.copy())
jogada.append(jogada3.copy())
jogada.append(jogada4.copy())
jogada.sort()
print(jogada)"""

#Fazendo com a ajuda com o professor
from random import randint
from time import sleep

#Essa função 'itemgetter' é fundamental para que o exercício seja resiolvido
# e os conteúdos sejam ordenados de forma diferente do dicionário 'jogo'
from operator import itemgetter
#primeiro ele importou a biblioteca de gerar números randomicos
#depois colocou de forma procedural os 'jogadores' e serus respectivos resultatos

jogo = {'jogador1' : randint(1, 6),
        'jogador2' : randint(1, 6),
        'jogador3' : randint(1,6),
        'jogador4' : randint(1,6)}

#Ele utilizou um outro local para para colocar os valores ordenados do maior para o menor
# interessante pensar nessa solução, pois eu não tive essa ideia... fiquei pensando que 
#deveria existir uma forma de reorganizar o dicionário original usando alguma estrutura de laço + condições

ranking= list()

print('Valores sorteados:')
for k,v in jogo.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)
#Nesse módulo nós vimos que os dicionário são separados em duas informações importantes 'Keys' e 'Values', 'Keys' são os índices e 'Values'os conteúdos
#desses respectivos índicesm. O 'itemgetter()' ele vai pegar esse dicionário e fazer uma verificação simpples usando '0' e '1'. 0 = 'Key' 1 = 'Value'
# e vai usar essa 'separação' que ele faz {porque meio que isso aki tas sendo tratado como um vetor... posição 0 = indice posição 1 = conteúdo} e vai pensar
#'Se for um 0 quer dizer índice... se for 1 quer dizer conteúdo'

print('Dessa forma ele só coloca em ordem crescente')
ranking = sorted(jogo.items(), key = itemgetter(1))
print(ranking)
print('-'*60)
print('adicionando o "reverse = True" você coloca ao inverso')
print('Dessa forma ele só coloca em ordem crescente')
ranking = sorted(jogo.items(), key = itemgetter(1), reverse = True)
print(ranking)
for i ,v in enumerate(ranking):
    print(f'{i} {v}')