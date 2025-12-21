#Escreva um progama que faça o computador 'pensar' em um número inteiro entre 0 e 5 e peça para
# o usuário descobiri qual foi o número escolhido pelo computador!
#o programa deverá escrever na tela se o usuário venceu ou perdeu
import random
import emoji
sorteado = random.randint(1,6) - 1
print('🤓💭---O computador pensou em um número entre 0 e 5...---🤓💭')
escolha = int(input('Entre com um número: '))
if sorteado == escolha:
    print('Você acertou! era esse mesmo 😔')
else:
    print('Você Errou! 🤭 \nO número era: [{}]'.format(sorteado))