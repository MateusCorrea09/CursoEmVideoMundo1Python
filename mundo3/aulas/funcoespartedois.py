def quebra_pagina():
    print('--'*90)
def titulo(msg):
    print('-='*3,msg,'-='*3)
titulo('Interactive Help')
#uma forma de documentação, que retorna um tipo de ajuda
#use o comando 'help()'
#help(enumerate)
#help(print)
#é uma forma de conhecer mais sobre alguma parte dp código, algo que vc não saiba e que o p´roprio python pode te ajudar esclarecendo
#como esse determinado recurso funciona, utilizando adocumentação desse recurso
print(input.__doc__) #uma outra forma de encontrar infromação sobre um rescurso
titulo('Docstring')
#todo comando do python possúi sua respectiva docstring, mas podemos criar nossas próprias funções e alimenta-la com uma
#documentdação criada por nós mesmos
#vamos ccriar um código de uma função para ser utilizada como um contador
def contador(i,f,p):
    """
    Docstring for contador
    Faz uma contagem a partir de uma série de entradas realizadas pelo usuário
    
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passos a serem contados
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}',end='..')
        c += p
    print('Fim!')
contador(2,10,2)
help(contador) #dessa forma será retornado tudo que há dentro do cotnador que está entre as 3 aspas
#então nós podemos criar nossa própria biblioteca de funções e documenta-la para me ajudar a lembrar
#ou ajudar outra pessoa que está usando

titulo('parâmetros opcionais')
print('Criando uma função "Somar" para o exemplo')

 # caso em ums função vc tiver um parâmetro que vc considere que talvez não haja uma entrada
 #você pode considerar ela como '0' e dessa forma o programa vai entender, que caso não receba nada... 
 #naturalmente determinado parâmetro terá '0' como variável 
 #Dessa forma evitando o erro
def somar(a, b, c = 0):
    total_soma = a + b + c
    print(total_soma)
somar(3,2,5)
somar(3,2)
titulo('Escobo de variáveis')

def teste():
    x = 8 #x é uma variavel local
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')

n = 2 #Mesmo que n esteja aqui em baixo, ele é reconhecido por todo o programa, inclusive pela função teste()
print(f'No programa principal, n vale {n}')
#print(f'No programa principal, x vale {x}') essa linha retornará um erro, porque x é uma variavel local dentro de teste()
#eu lembro que iso faz mais sentido em línguagens que tem '{}' como identação... porque fica visível onde acaba e termina as coisas
titulo('Criando uma função que considera variaveis globais')
def teste_global(b):
    global a #aqui vc silaniza pro programa que há uma variavel global que tem o mesmo nome que 'a' dessa forma ele tem que usar o 'a' global e não criar uma variavel local chamad 'a'
    a = 8 
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')
a = 5
teste_global(a)
print(f'A função fora vale {a}')

titulo('Rertorno de valores usando o return')
print('usando como exemplo a função somar desenvolvida anteriormente')
def somar(a, b, c = 0):
    total_soma = a + b + c
    print(total_soma)
somar(3,2,5)
somar(3,2)
print('Todos eles retornam prints de tela, e não um resultado')
def somar(a, b, c = 0):
    total_soma = a + b + c
    return total_soma
#somar(3,2,5) essa escrita anteriormente usada vai dar erro, pois a função Retorna uma coisa... logo essa mesma deve ser salva em algum lugar
resposta = somar(3,2,5) #agora o return esta salvo dentro de resposta, e pode ser utilizado para qualquer fim necessário
print(somar(3,2,5)) #ou dasse forma, na verdade que quero que a função me retorne um resultado, não que ela só escreva de uma forma específica

