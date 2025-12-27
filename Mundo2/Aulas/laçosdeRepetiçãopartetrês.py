#em determinadas sotuações é necessário persolalizar a estrutura de repetição
#para que haja desvios de percurso e dessa forma conseguir parar um determinado
# loop. para isso usamos algumas nomenclaturas como break, continue ou pass
# utilizamos o 'break' para sinalizar para o programa que desejamos que o fluxo
# no qual o programa está correndo seja parado e que saia do loop/estrutura  caso
# determinado resultado aconteça 
#um exemplo disso seria: 
#While True:
#   faça_algo()
#   if 'algo':
#       break
# Nesse exemplo acima, o loop acontecerá infinitamente, mas de determinada situação
# resultar em uma verdade ele será interrompido pelo 'break' e o loop será finalziado

#Exemplo em aula
#Nesse exemplo enquanto a condição dentro de while for verdade o loop acontecerá
# e permitirá ser contado e printado em tela até 10
#print('---Aplicação teste---')
#cont = 1
#while cont <= 10:
#    print(cont, '-> ', end ='')
#    cont += 1
#print('---fim da aplicação teste---')

#Agora, se trocassemos a condição para 'True' ele entrará em um loop infinito que só
#será parado a partir de uma ação manual do usuário, clicando no botão de stop no programa
#print('---Aplicação teste---')
#print('---usando o "True" como condição do loop')
#cont = 1
#while cont True:
#    print(cont, '-> ', end ='')
#    cont += 1
#print('---fim da aplicação teste---')
#para resolver esse problema podemos usar o break!

#print('---Aplicação teste---')
#No exemplo abaixo, o código contabiliza a flag de parada, que seria 999
# e o deal é utlizar uma condição de parada para que o '999' não seja contabilziado
#na soma total dos valores
#n = soma_total = 0
#while n != 999:
#    num = int(input('Entre com um n: '))
#    soma_total += num #nessa parte tem um erro que acontece, o '999' é contabilizado no somatório... mas o programa não avisa que isso se trata de um erro
#print('A soma total dos valores é de [{}]'.format(soma_total))
#print('---fim da aplicação teste---')

#No exemplo abaixo trocamos a condição de parada por 'True' e inicialemnte
#  pensamos que isso levará a um loop infinito
#print('---Aplicação teste---')
#print('---usando o "break" como condição de parada---')
#n = soma_total = 0
#while True:
#    num = int(input('Entre com um n: '))
#    if num == 999:
#        break #utilizan do o break ele quebra o loop do 'while True' e não contabiliza o '999'
#    soma_total += num 
#print('A soma total dos valores é de [{}]'.format(soma_total))
#print('---fim da aplicação teste---')

#print('---Aplicação teste---')
#print('--- ---')
#n = soma_total = 0
#while True:
#    num = int(input('Entre com um n: '))
#    if num == 999:
#        break 
#    soma_total += num 
#print('A soma total dos valores é de [{}]'.format(soma_total))
#print('---fim da aplicação teste---')