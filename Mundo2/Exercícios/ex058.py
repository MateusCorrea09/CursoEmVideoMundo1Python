#Melhore o jogo do DESAFIO 028, onde o computador vai 'Pensar' em um número entre 
#o e 10, Só que agora o jogador vai tentar até adivinhar e acertar, mostrando no
#final a quantidade de palpites necessários para vencer o desafio.
import random
from time import sleep
maquina_pensa = random.randint(1,10)
entrada = int(input('A maquina está pensando em um número! entre com um palpite dentre (1 - 10): '))
print('Será esse número mesmo?')
sleep(1)
while entrada != maquina_pensa:
    entrada = int(input('Você errou! entre com um palpite novamente entre (1 - 10): '))
    print('Será esse número mesmo????')
    sleep(0.5)
print('Você acertou! a maquina pensou no mesmo número que você [{}]'.format(maquina_pensa))