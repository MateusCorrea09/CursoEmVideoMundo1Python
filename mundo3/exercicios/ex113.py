#Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a
#  possibilidade da digitação de um número de tipo inválido. Aproveite e crie
#  também uma função leiaFloat() com a mesma funcionalidade.

def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('Erro por favor digite um número inteiro válido')
            continue
        except KeyboardInterrupt:
            print('O usuário preferiu não digitar esse número')
            return 0
        else:
            return n
def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('Erro por favor entre com um número ponto flutuante válido')
            continue
        except KeyboardInterrupt:
            print('O usuário preferiu não digitar esse número:')
            return 0
        else:
            return n

num = leiaint('Digite um valor: ')
print(f'O valor digitado foi {num}')
num = leiafloat('Entre com um valor ponto flutuante: ')
print(f'O valor digitado foi {num}')