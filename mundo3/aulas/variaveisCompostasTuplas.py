#Tuplas são estruturas de dados que possuem característica composta
# isso significa que elas podem guardar um número X de conteúdos dentro
# existem outros tipos de variaveis compostas, mas hoje falaremos sobre tuplas.
#---Acessando conteúdos dentro de uma tupla pelo índice---
# os conteúdos dentro da Tupla podem ser acessados a aprtir de um índice, eles são
# inteiros.
# ex: 
#lanche = ('bolo', 'biscoito', 'hamburguer', 'camarão', 'churrasco') # nesse exemplo o biscoito está localizado 
# índice '1' da tupla, com isso, podemos pritar na tela como print(lanche[1])... é bem similar
#--Fatiamento em Tuplas--
# a como as strings funcionam e como os vetores no Java (mas as tuplas tem outras características)
# da mesma forma que o fatiamento em uma string pode printar na tela um determinado intervalo de
# conteúdos pertencentes a uma string, em uma tupla é possível realizar a mesma ação, através do
# print(lanche[0:2]) e dessa forma serão printados na tema 'bolo' e 'biscoito' já o item pertencente
# índice '2' que seria o 'hambuguer' ele será excluído no print já que essa forma de fatiamento excluí
# o ultimo índice.
# através desse
#print(lanche[1:]) #Serão exibidos na tela dês do índice 1 até o ultimo conteúdo dentro de uma string
#---Tuplas índices negativos---
# Em alguns exemplos  você pode encontrar 'lanche[-1]' isso siginfica que ele está acessando os índices de trás para frente
# então será exibido na tela 'churrasco', se aocntecer um print(lanche[-3]) será exibido 'hamburguer'
#print(lanche[-3])
#--- Estruturas de repetição ---
#podem ser usadas para acessar algum índice e exibir o resultado um número determinado de vezes por esemplo!
#for i in lanche: #Nesse exemplo serão capturados cada elemento um por vez e exibido na teala através da variavel 'i'
#    print(i)
#--- Funções ---
# através do 'len()' é possível retornar o tamanho de uma tupla, com o exemplo:
#print(len(lanche))#  e será exibido 5

#---Características da tupla! ---
#Tuplas são imutáveis
# *Isso significa que depois de declaradas, são é possível alterar um conteúdo dentro de uma tuplam, ou adicionar um novo.
#lanche[1] = 'pão de queijo' #isso aki vai dar erro :D


#Aula prática
#tuplas sempre começam com '()'
#é i mportante ter em mente que tuplas são variaveis compostas, e isso soginfica que elas guardam mais de um conteúdo, no sentido de que
# se queriamos declar que uma variavel 'lanche' receberia varios tipos de lanches... fariamos anteriormente dessa seguinte forma
print('---Variaveis simples')
lanches = 'hamburguer'
print(lanches) #será exibido 'hamburguer'
lanches = 'suco' # "ADICIONAMOS" o conteúdo 'suco'
print(lanches) #será exibido 'suco' ao invés de lanche, não mais o 'hamburguer'
print('---Fim do exemplo das variaveis simppls---\n')
#isso siginifica que 'lanches' se trata de uma variavel simples, que guarda apenas um conteúdo por vez
lanche = ('Hamburgeur', 'Suco', 'Pizza', 'Pudim') # nesse caso declaramos uma variavel composta chamada 'lanche' e atribuimos a ela dois conteúdos
print('---Variaveis compostas, exemplo---')
print(lanche)# E serão exibidos 'Hamburgeur', 'Suco', 'Pizza'e 'Pudim'
print('---Fim do exemplo das variaveis simppls---\n')
#podemos exibir índices negativos indo de trás para frente
print('índice negativo: [-2]')
print(lanche[-2]) #será exibido "pizza"
print('fatiamento [1:3]')
print(lanche[1:3]) # serão ezibidos 'Suco' e 'Pizza'... o índice '3' será excluído
print('exibindo de uma aparte até o final')
print(lanche[2:]) # será exibido a aprtir do índice 2 até o ultimo conteúdo dentro da tupla, dessa forma consideranto o úmtimo índice
print('Exibindo do ínicio até o elemento específico')
print(lanche[:2]) # Serão exibidos os elementos dês do 0 até o elemnto 2, dessa forma excluíndo o elemnto 2
#acho que nesse último talves seja ideal ter em emnte que índices negativos possam aparecer nos exercícios
# então lembrese de que:
print('print na tela do índice lanche[-2]')
print(lanche[-2])
print('print na tela de umas sequência de elemtnos a aprtir do [-2] até o "Final" - > lanche[-2:] ')
print(lanche[-2:]) #serão exibidos 'Pizza' e 'Pudim'
print('exibindo o conteúdo inteiro:')
print(lanche)
print('Reorganizando uma Tupla, usando o método "sorted()"')
print('tupla reorganizada {}\nTupla em seu estado natura {}'.format(sorted(lanche), lanche)) #O 'sorted()' reorganizou a tupla em uma lista, por conta disso ela é exibida com '[]' ao invés de '()'
print('\n')
a = (2,5,4)
b = (5,8,1,2)
print('Tuplas com numeros:')
print(f'Tupla A = {a}')
print(f'Tupla B = {b}')
print('Unindo as duas em uma nova tupla A+B:')
c = a + b
print(f'Tupla C = {c}')
print('A ordem das adições altera o resultado! ')
print('Unindo as duas em uma nova tupla B+A:')
d = b + a
print(f'Tupla D = {d}')
print('\n')
print('Conte quantas vezes um elemnto aparece dentro de uma tupla:')
print('Quantas vezes o "2" Aparece dentro da tupla C ?')
print(c.count(2))
print('Use o "index" para descobriur qual é a posição de um determinado elemento den tro da tupla')
print(f'Em que posição o elemento 2 está na tupla C ? : {c.index(2)}')

#---Fim da parte prática da aula---