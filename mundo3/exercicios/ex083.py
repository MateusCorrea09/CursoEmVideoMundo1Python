#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos
# e fechados na ordem correta.


###OBSERVAÇÃO PRA QUEM TA LENDO ISSO,,, 
"""
Eu tentei criar uma pilha de true e false... lembroq ue já fiz isso em Java e deu certo, mas se vc entra com uma string como
entrada = (2+2(++++) vai dar erro
porque em python strings são imutaveis, e isso significa que quando chegar na primeria verificação ele não consegue alterar o
ultimo aprênteses para '0' então esse ultimo aprenteses sempre vai ficar ali e contando como válido...
minha ideia era pegar os '(' e a aprtir deles ir verificando se há ')' e assim troca-los por '0' e dessa forma a pilha iria funcionar
mas strings são imutaveis

então minha ideia final é fazer um entrada.cont() e se retornar um valor par para '(' e para ')' quer dizer que ta tudo ok
"""


entrada = str(input('Entre com sua expressão:\n '))
aberto = False
fechado = False
for indice, i in enumerate(entrada):
    if indice == 0 and i == ')':
        fechado = True
        break

    elif i == ')' and aberto != False:
        print('Há um aprenteses posicionado da forma Errado :D')
        break

    elif i == '(':
        aberto = True
        #for j in range(indice, len(entrada) - 1):
        for j in entrada:
            if j == ')':
                aberto = False
                fechado = False
                break

#print(fechado)
if aberto == False  and fechado == False:
    print('sua expressão esta correta!')
else:
    print('Sua expressão esta com parênteses posicionados de forma incorreta')    
print('\n')
print('*'*30)
print('VERIFICAÇÃO FINAL CORRETA !!!!!')
print('*'*30)
abre = entrada.count('(')
fecha = entrada.count(')')
if abre % 2 ==0:
    aberto = False
else:
    aberto = True
if fecha % 2 ==0:
    fechado = False
else:
    fechado = True
if aberto == False  and fechado == False:
    print('sua expressão esta correta!')
else:
    print('Sua expressão esta com parênteses posicionados de forma incorreta')
#observação, eu vou ver oq o professor fez para resolver esse :D
#PELO QUE EU ENTENDI ELE TBM USOU O CONCEITO DE PILHA, MAS ARMAZENOU EM UMA VARIAVEL AUXILIAR, sorry pelo cps