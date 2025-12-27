#Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador.
#  O jogo só será interrompido quando o jogador perder, mostrando o total de
#  vitórias consecutivas que ele conquistou no final do jogo.
import random
while True:
    entrada_usuario = int(input('Entre com um valor: '))
    entrada_computador = random.randint(1,9)
    escolha= str(input('Entre com uma das alternativas:\n[P] - par\n[I] - ímpar\n')).upper()
    resultado = entrada_computador + entrada_usuario
    if resultado % 2 ==0:
        resp = 'P'
    else:
        resp = 'I'
    if escolha == resp:
        print('[{}] Vitória do jogador! o resultado é [{}]'.format(resultado,resp))
    else:
        print('[{}] Vitória do computador! o resultado é [{}]'.format(resultado,resp))
    resposta = str(input('Deseja continuar [S / N]? ')).upper()
    if resposta == 'N':
        break
print('Fim da aplicação! obrigado por jogar :D')