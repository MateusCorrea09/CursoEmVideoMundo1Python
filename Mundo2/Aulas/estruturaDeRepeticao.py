#Essas estruturas são fundamentais para construir um número de interações deliminatas, chamado laço de controle
#essa seria a diferença entre a escrita na nossa linguagem e a o Python
#laço c no intervalo(1,10)      #   for c in range(1,10):
#   pesso                       #       passo()
#pegar                          #   pegar()

#no python você pode alinhar estruturas dentro de outras estruturas usando por exemplo 'if' dentro de um 'for'
nome = 'Mateus'
print('---início da aplicação---')
for i in range(0,3): #é importante lembrar que a contegem é realizada até o índice 2... o 3 fica de fora
    if nome == 'Guanabara':
        print('Professor')
    print(nome)
print('---Fim da aplicação---\n')

#você pode solicitar que o loop realize uma iteração ao inverso! usando uma inofrmação adicional dentro do Range
# assim o loop entenderia que ele precia 'Contar para trás'
print('---início da aplicação---')
print('---Contando de trás pra frente---')
for i in range(6,0,-1):
    print(i)
print('---Fim da aplicação---\n')

#Em alguma determinada situação taçvez seja necessário pular um determinado índice da contagem, então você pode posiconar
#no range uma informação que diz o numero de casas que serão puladas na hora de realizar um loop.
#pulando uma casa
print('---início da aplicação---')
print('---contando uma casa e pulando a seguinte---')
for i in range(0,7,2): # esse '2' no terceiro índice dentro do range significa o 'pular de casa'.. então ele vai contar uma casa e a seguinte seá pulada
    print(i)
print('---Fim da aplicação---\n')
#pulando 2 casas:
print('---início da aplicação---')
print('---contando duas casa e pulando as duas seguintes---')
for i in range(0,7,3): # esse '3' no terceiro índice dentro do range significa o 'pular de casa'.. então ele vai contar uma casa e as duas seguintes serão puladas
    print(i)
print('---Fim da aplicação---\n')

#O interessante que você pode também pedir para que o usuário entre com um dado a ser utilizado dentro de um loop
print('---início da aplicação---')
print('---contandaté o número digitado pelo usuário---')
n = int(input('Entre com um número inteiro: '))
#eu consigo ler um valor e usar ele dentro do 'range()'
for i in range(0,n + 1):
    print(i)
print('---Fim da aplicação---\n')

#levando em consideração que esse 'range' é formdo por range([ponto de partida], [ponto de parada], [Condição de leitura]):
#da pra gente pedir pro usuário entrar com toas as informações para o loop de for ser utilizado
print('---início da aplicação---')
print('---Entrando com todas as informações:---\n range([ponto de partida], [ponto de parada], [Condição de leitura])\n')
inicio = int(input('Entre com o início: '))
fim = int(input('Entre com o fim: '))
condicao = int(input('Entre com o nº referente as casas puladas: '))
for i in range(inicio,fim + 1,condicao): #coloquei o '+1' depois do 'fim' para ele ler até o número digirado pelo usuário
    print(i)
print('---Fim da aplicação---\n')

print('---início da aplicação---')
print('---Calclando uma soma total!:---')
soma_total = 0
for i in range(0,4):
    #aqui eu pego a entrada do usuário, que vai ser um inteiro
    entrada_usuario = int(input('Entre com um número: '))
    #aqui eu pego o que já tem dentro de 'soma_total' e adiciono o que o
    #usuário entrou, e depois coloco dentro de 'soma_total' que é uma variavel
    #que está fora do loop armazenando as informações
    soma_total = soma_total + entrada_usuario
print('A soma de todas as entradas foi [{}]'.format(soma_total))
print('---Fim da aplicação---\n')