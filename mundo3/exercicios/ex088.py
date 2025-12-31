#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos
#  serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
#eu tenho que perguntar quantas jogos a pessoa vai jogar
from random import randint
import time
lista_numerica = list()
#entrada = int(input('Quantos jogos deseja jogar?'))
#cont_jogos = entrada

# ai eu tenho que depois pegar esse numero e usar o while true para ficar perguntando para ele... deseja jogar mais? se sim
# eu volto a pergunatr quantos jogos ele vai jogar

while True:
    resposta = str(input('Deseja jogar mais jogadas?[s/n] ')).lower()
    if resposta == 'n':
        print('--fim da aplicação--')
        break
    entrada = int(input('Quantos jogos deseja jogar?'))
    for j in range(0, entrada):
        for i in range(0,6):
            lista_numerica.append(randint(0,60))
        print(lista_numerica)
        time.sleep(1)
        lista_numerica.clear()