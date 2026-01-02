#Funções são rotinas no sistema, essas mesmas são referenciadas quando precisamos fazer algo... e esse algo pode ser feito
# ou necessário ser feito várias vezes, então criamos um trecho de código que pode ser reutlizado em momentos de 
# necessidade.
# print() ou len() são funções no python, elas jpa vem no sistema então vc não precisa pega-las de fora do sistema.
# exemplo de utlidade, talvez seja ideal criar uma função para exibir uma linha na tela, então pdoemos criar algo assim
# que pode ser utlizada no sistema
print('-'*30)
print('Meu nome é Mateus!')
print('-'*30)

#ao invés de usar uma escrita longa, colcoando print várias vezes, podemos criar uma função que realiza essa escrita
#que divide as informações, dessa forma nós polpamos código. Dessa forma eu posso criar comandos personalizados
def linha():
    print('--'*30)

linha()
print('A função sendo utlizada')
linha()
#   iniamos a escrita da rotina colocando o 'def' logo ewm seguida o nome da torinha junto com o '()' e ':'
#uma torina pode ter ou não um return.

#   além de apenas printar linhas, uma forma de personalziar ainda mais podemos passar os 'Parâmetros' que seria passar uma
#informação para ser utilziada na rotina... é quese como se fosse uma receita de bolo... que para ser feita ela 'espera' alguns
#ingredientes e sempre vai retornar de uma forma o bolo (que no caso seria o return), os 'parâmetros' são os ingredientes que
#a rotina espera.

#   Abaixo eu fiz uma rotina (uma receita) que retorna uma mensagem personalizada para o usuário... só que para retornar a mensagem 
#para o usuário é necesssário passar como 'ingrediente' uma variavel que contém alguma infoemação a ser exibida na tela...
# pois se trata de uma função que retorna uma mensagem :D
#Em python a língua não é tipada, isso significa que eu posso passar qualquer coisa como parâmetro na função que ela vai tentar fazer
#o que ela faz.... eu sei que isso é esqusito. O ideal é que passamos uma mensagem em String para ser exibida na tela, mas como a linguagem
#não é tipada isso significa que se passarmos um 'int' ou 'boolean' ele vai pegar isso e exibir no lugar de 'msg'
def mensaem_linha(msg):
    print('-'*90)
    print(msg)
    print('-'*90)

x ='Teste de função que recebe uma string como parâmetro'
mensaem_linha(x)
y ='Teste de uma função que recebe um "int" como parâmetro:'
mensaem_linha(y)
a = 58
mensaem_linha(a)
ponto = 'a questão de "a função vai tentar fazer oq ela tem que fazer com qualquer coisa que vc passar por parâmetro" isso faz mas sentindo em uma linguagem tipada, então eu recomendaria vc ... isso vc mesmo :D procurar como fazer funções com java pois java é uma linguagem tipada e eu acho que a compreenção é mais eficiênte com uma linguagem tipada'
mensaem_linha(ponto)
def linha_base():
    print('-'*90)
def linha_titulo(x):
    print(f'\n---{x}---\n')
linha_base()
mensaem_linha('parte prática da aula')
linha_base()
linha_titulo('Veremos um exemplo em que usaremos 3 variaveis A, b e S\n e realizaremos o calculo dos números que elas possuem')

a = 4
b = 5
s = a + b
print(f'{a} + {b} = {s}')
a = 8
b = 9
s = a + b
print(f'{a} + {b} = {s}')
#   Perceba que estamos realizando uma tarefa duas vezes, e essa mesma pode ser requisitada em outros momentos
#logo podemos pegar essa tarefa e atribuir ela a uma 'rotina' e a partir disso polparmos código no nosso
#sistema
#   Criaremos uma rotina chamada 'calculo_soma' que espera como parâmetro dois valores quais quer, e essa mesma
# realizada a soma desses dis valores e mostrará na tela
def calculo_soma(primeiro_valor, segundo_valor):
    print(primeiro_valor + segundo_valor)
linha_titulo('Criamos uma função que pega dois valores e realiza a soma deles, retornando como print an tela')
a = 2
b = 5
print(f'A = {a} B = {b}')
calculo_soma(a,b)
#podemos até mesmo passar esses mesmos valores dentro da construção da função
#exemplo:
calculo_soma(2,5)
#O que interessa para a função é que no seu argumento esteja dois valores
linha_titulo('Coloando uma string dentro do argumento')
print(f'A = "2" B = "5"')
calculo_soma('2','5')
#como essa função está esperando dois valores quis quer, se vc passar duas strings ela vai juntar as duas, formando 25
linha_titulo('Passando um boolean como parâmetro')
calculo_soma(True,True) # 1 + 1
calculo_soma(False,False) # 0 + 0
calculo_soma(True,False) # 1 + 0
calculo_soma(False,True) # 0 + 1

linha_titulo('Alterando a ordem dos argumentos, sem alterar o resutlado A = 2 B = 7')
#você pode alterar a ordem dos argumentos contanto que vc deixe explicito qual determinado valor pertence ao oq está
#sendo aguardado... isso pode ficar confuso mas se atente ao exemplo abaixo
#calculo_soma() espera dois parâmetros no seu argumento 'primeiro_valor' 'segundo_valor'
#a depender da situaçãoq em que uma função está sendo declarada, talvez a ordem das coisas seja realmente improtante
#por conta disso podemos passar como parâmetro qual determinado valor pertence ao determinado parâmetro
#exemplo:
a = 2
b = 5
calculo_soma(a,b) #Nesse exemplo a pertence ao 'primeiro_valor' e b pertence ao 'segundo_valor'
calculo_soma(b,a) #Nesse exemplo b pertence ao 'primeiro_valor' e a pertence ao 'segundo_valor'
calculo_soma(primeiro_valor = a, segundo_valor = b) #Nesse exemplo, nós deixamos claro quem pertence a quem, evitando erros

linha_titulo('Testando o "Empacotamento" no python')
#é basicamente uma forma de criar uma função que não tem um numero definido como parâmetos a serem aguardados para a função ser executada.
#isso significa que o usuário pode digitar um número X de entradas e as passar como argumentos
#Exmplo, a função abaixo serve para contar quantos números foram passados pelo usuário

def contador(*num): #Essa parte '*num' seria meio que... eu não sei oq vai vir ae :D mas faz oq tem que fazer
    print(f'Recebi {len(num)} números e são {num}')
contador(2,6,9,11,2,0,7)
contador(3,7,1)
contador(0000,1,2)

linha_titulo('Realizando soma de diversas entradas')
def soma_valores(*num): #Importante resaltar que aqui ele trabsforma as entradas em um 'Pacote'... que seria uma tupla
    total_soma = 0
    for i in range(0,len(num)):
        total_soma +=num[i]
    print(total_soma)

soma_valores(1,2)
soma_valores(3,4)
soma_valores(1,2,3,4,5)
soma_valores(9, 8 , 7)

linha_titulo('Usando funções apra trabalahr com listas!')
valores = [7,2,5,0,4]
#Você pode passar uma lista como parâmetro
def dobra_valores_lista(lista):
    for i in range(0,len(lista)):
        lista[i] = lista[i] * 2
    print(f'A Lista com valores dobrados é {lista}')
dobra_valores_lista(valores)
