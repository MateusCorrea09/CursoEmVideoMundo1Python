#Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de
#  visualização de detalhes do aproveitamento de cada jogador.
jogador = dict()
jogadores = list()
partidas_gols = list()
total_gols = 0
while True:
    jogador['nome'] = str(input('Entre com o nome do jogador: '))
    jogador['partidas'] = int(input(f'Quantas partidas o jogador [{jogador["nome"]}] jogou?'))
    for partidas in range(0,jogador['partidas']):
        cont_gols = int(input(f' Entre com o Nº de gols da partida[{partidas + 1}]: '))
        partidas_gols.append(cont_gols)
        total_gols += cont_gols
    jogador['partidas_gols'] = partidas_gols[:] #sempre se lembrar de usar '[:]' porque vc ta criando uma cópia a partir da lista
    jogador['total_gols'] = total_gols
    total_gols = 0
    partidas_gols.clear()
    jogadores.append(jogador.copy())
    jogador.clear()
    resp = str(input('  Deseja continuar[S / N]?')).lower()
    if resp == 'n':
        break    

while True:
    print('='*30)
    for i,conteudo in enumerate(jogadores):
        print('---'*30)
        for key, value in conteudo.items():
            print(f'{i} : {key}  [{value}]',end='')
        print()
        print('---'*30)
    print('='*30)
    resp = int(input('  Deseja saber mais sobre o desempenho de qual jogador[*999 encerra*]?'))
    if resp == 999:
        break
    else:
        print('='*90)
        print(jogadores[resp])
                
