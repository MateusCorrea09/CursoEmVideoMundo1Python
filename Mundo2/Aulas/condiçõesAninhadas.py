#estrutura de controle mais aprofundada :D
#aninhar -> colocar uma coisa dentro da outra
#no 'if' e 'else' só temos verdadeiro ou false representados
#aninhar em 'if' e 'else' seria posicionar uma etrutura condicional dentro de outra
#com o objetivo de ter mais opções e cobrir um leque maior de possibilidades
#uma forma de representar essa ideia é umas o 'elif' (que é uma estrutura que eu usei em um exercícios anterior)
# if: -> elif: ->else: essa estrutura é para 3 opções
# se você precisar usar mais de 3 opções você adiciona mais um 'elif' e assim por diante

#apresentação prática do conteúdo:
nome = str(input('Qual seu nome?')) #utilziando um exercício anterior para explicar o conceito de 'elif'
if nome == 'Gustavo':
    print('Que nome bonito')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Rogério':
    print('Seu nome é bem popular no Brasil')
elif nome == 'Calaudia' or nome == 'Jurandir' or nome == 'Zé':
    print('Seu nome é bem velho')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, [{}]!'.format(nome))