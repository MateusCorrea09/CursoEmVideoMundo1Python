#Crie um programa que faça o computador jogar Jokenpô com você.
import random
from time import sleep
entrada_usuario = int(input('Entre com uma das alternativas abaixo:\n1 - Pedra\n2 - Papel\n3 - Tesoura\n'))
escolha_maquina = random.randint(1,3)
##sleep(num) professor mostrou esse recuro... achei interessante :D
print('JO')
sleep(1)
print('KEM')
sleep(1)
print('PO!!')
if entrada_usuario == escolha_maquina:
    print('Usuário escolheu [{}] e a Maquina escolheu [{}]'.format(entrada_usuario,escolha_maquina))
    if entrada_usuario == 1:
        print('Pedra com Pedra!')
    elif entrada_usuario == 2:
        print('Papel com Papel! não da em anda')
    elif entrada_usuario == 3:
        print('Tesoura com tesoura!')
##
elif entrada_usuario == 1 and escolha_maquina == 3:
    print('Usuário [Pedra] maquina [tesoura]\n Vitória do usuário!')
elif entrada_usuario == 2 and escolha_maquina == 1:
    print('Usuário [Papel] maquina [Pedra]\n Vitória do usuário!')
elif entrada_usuario == 3 and escolha_maquina == 2:
    print('Usuário [Tesoura] maquina [papel]\n Vitória do usuário!')
    ##
elif escolha_maquina == 1 and entrada_usuario == 3:
    print('Maquina [Pedra] Usuário [tesoura]\n Vitória da Maquina!')
elif escolha_maquina == 2 and entrada_usuario == 1:
    print('Maquina [Papel] Usuário [Pedra]\n Vitória da Maquina!')
elif escolha_maquina == 3 and entrada_usuario == 2:
    print('Maquina [Tesoura] Usuário [Papel]\n Vitória da Maquina!')