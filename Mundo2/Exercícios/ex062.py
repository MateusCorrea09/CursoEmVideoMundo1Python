#n1 = int(input('Entre com um número: '))
#razao = int(input('Entre com a razao: '))
#cont = 0
#conteudo = 0
#resposta = 's'
#contador_comparativo = cont
#while resposta == 's':
#    while cont != contador_comparativo:
#        conteudo = n1 + (cont + 1) * razao
#        cont = cont + 1
#        print(cont,conteudo)
#    resposta = str(input('Deseja continuar? [s / n] ?')).lower()
#    if resposta == 's':
#        contador_comparativo = contador_comparativo + 10

#relendo o exercício e vendo a resolução do professor, ele disse que o usuário deve entrar com um número
# de progressão que ele deseja ver... de forma adicional... então quando ele entrar com 0 o programa para
primeiro = int(input('Entre com um número: '))
razao = int(input('Entre com a razao: '))
termo = primeiro
resposta = 10
cont = 1
total = 0 #armazena a infomação ciclo após ciclo
while resposta != 0:
    total = total + resposta #soma a resposta com o final do ciclo
    while cont <= total:# usa o contador para contar até o ciclo, nessa parte pode ocorrer um problema de lógica
        #caso o 'cont' estivesse fora do código, mas essa variavel tbm é 'global' e está sendo atualizada tbm, então ele para no ultimo ciclo armazena o contador e começa de onde parou ontando até o próximo limite definido
        print('{} ->'.format(termo),end='')
        termo += razao
        cont += 1
    print('Pausa!')
    resposta = int(input('Quantos termos deseja a mais? '))
print('Fim')
