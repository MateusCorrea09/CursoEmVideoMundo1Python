#refaça o desadio 009, mostrando a tabuada de um número que o usuário
#escolher, só que agora utilizando um laço for
entrada = int(input('Entre com um número: '))
for i in range(0,10 + 1):
    print('[{}] * [{}] = [{}]'.format(entrada,i,entrada*i))