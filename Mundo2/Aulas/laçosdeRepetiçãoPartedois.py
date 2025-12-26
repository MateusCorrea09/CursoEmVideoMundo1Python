#estrutura de repetição While
#essa é uma estrutura utilizada para as situações em que não sabemos o 
#limite das aç~es a serem tomadas, de forma a se diferenciar do 'for'
# em nossa língua podemos dizer algo do tipo 'Enquanto determinada cosia não acontecer... faça algo'
#é sempre nesse 'Enquanto', em programação o 'While' se chama Estrutura de repetição com teste lógico
#enquanto não for possível fazer uma determinada ação:   #  while not apple:
#    faça()                                              #      passo()
#realize tal ação()                                      #  pega()

#parte prática
#Exemplo com o for:
#for c in range(1,10):
#    print(c)
#print('fim')
#Exemplo com o while, quando eu sei o limite
#c = 1 #note que tem uma variavel criada separadamente 
#while c < 10:
#    print(c)
#    c = c + 1 #A contagem é feita dento do loop, differente do for que ocorria na estrutura de declaração
#print('fim')
#Exemplo com while, quadno eu não sei o limite:
#Em um exemplo simples de loop, imagine que vc deseja que o usuário entre com vários números, e dentre essas entradas, se
#o correr uma entrada do tipo '0' o programa deve parar... nesse caso o 'limite' é desconhecido, então essa situação pede
#uma estrutura de repetição do tipo 'WHILE'
#print('---Aplicação: Entre com um número diferente de 0, e se entrar o programa sera finalizado! ---')
#n = None #comecei com 'None' como um tipo de variavel não inicializada ainda
#while n != 0: #condição de parada
#    n = int(input('Enre com N:'))
#print('---Fim da aplicação exemplo!---')

#print('---Aplicação: Entre com uma resposta! ---')
#r = 's' #aqui eu precisei começar com 's'
#while r == 's': #condição de parada, a entrada precisa ser 's' para continuar
#    r = str(input('Enre com R:')).lower()
#print('---Fim da aplicação exemplo!---')

#mas podemos usar uma verificação como se fosse um sistema perguntando algo para o usuário
#utilizando os dois exemplos acima
print('---Aplicaçãoe estilo menu!---')
r = 's'
while r == 's':
    n = int(input('ENTRE COM UM NÚMERO: '))
    r = str(input('Deseja continuar [s / n]: ')).lower()
print('--Fim da aplicação estilo menu!---')

print('---Aplicação de verificação e contagem de entradas!---')
n = None
cont_pares = 0 #diferente do 'n' acima eu não posso colocar 'None' nessa variavel do tipo contadora... porque lá no loop ela começa pegando o que já tem dentro dela e realizando um calculo... logo não pode fazer isso! ela tem que começar com '0'
cont_impares = 0#isso vale pra essa tbm
while n !=0:
    n = int(input('Entre com um numero: '))
    if n != 0:
        if n % 2 == 0:
            cont_pares = cont_pares + 1
        else:
            cont_impares = cont_impares + 1
print('O número de entradas pares é [{}]\ne o número de entradas ímpares é [{}]'.format(cont_pares,cont_impares))
print('---Fim da aplicação!---')