#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador 
# e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso
#  será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
jogador = dict()

jogador['nome'] = str(input('Entre com o nome do jogador: '))
jogador['partidas'] = int(input(f'Quantas partidas o jogador [{jogador["nome"]}] jogou?'))
total_gols = 0
partidas_gols = list()
for partidas in range(0,jogador['partidas']):
    cont_gols = int(input(f' Entre com o Nº de gols da partida[{partidas + 1}]: '))
    partidas_gols.append(cont_gols)
    total_gols += cont_gols
jogador['partidas_gols'] = partidas_gols[:] #sempre se lembrar de usar '[:]' porque vc ta criando uma cópia a partir da lista
jogador['total_gols'] = total_gols
print('-'*60)
for key,value in jogador.items():
    print(f'{key} tem valor -> {value}')
print('-'*60)
for i in range(0,len(partidas_gols)):
    print(f'no jogo [{i + 1}] o jogador teve {partidas_gols[i]} gols')