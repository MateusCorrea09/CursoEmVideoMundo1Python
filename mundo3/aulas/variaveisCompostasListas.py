#diferente das tuplas as litas são 'Mutaveis' elas podem ser alteradas a través de comandos
# são caracterízadas pelo uso de '[]' colchetesm e a estrutura de armazenamento e de acesso é igual, através de índices
# são variaveis compostas, guardam muitos valores
# para adicionar um novo item a uma lista você deve usar o '.append()' quer funciona como uma pilha adicionando no final da lista
print('---Adicionando itens a lista---')
print('---Utilizando o ".append()"---')
lanche = ['hamburguer','suco', 'pizza','picole']
print(f'Lista de lanches = {lanche}')
print('.append("Bicoito")')
lanche.append('biscoito') #adiciona um novo item no final da lista
print(f'Lista de lanches = {lanche}')
print('\n')
#O método inserte permite que o usuário insira um novo item na lista com base em duas informações
#a posição que ele pretende inserir o item e o cotneúdo a ser adicionado na lista.
# é importante ter em mente que quando isso acontece todos os itens são deslocados uma casa para frente  
print('---Utilizando o ".insert(posição,item)"---')
print(f'Lista de lanches = {lanche}')
print('.insert("cachorro-quente")')
lanche.insert(0,'cachorro-quente') #adiciona um novo item em uma posição específica da lista, empurando todos os outros itens uma cada para frente
print(f'Lista de lanches = {lanche}')

print('---Fim dos métodos de adição---')
print('\n')
print('---Apagando itens da lista---')
print('Utilizando o comando "del" ')
print('del lanche[3]')
print(f'Lista de lanches = {lanche}')
del lanche[3]
print(f'Lista de lanches = {lanche}')
print('\n')
print('Utilizando o método ".pop(3)" ') #Esse método me lembra mais o comando que eu usava quando estava estudando estrutura de dados na faculdade
print('lanche.pop[3]')                  #Esse método é utlizado para elimitar no ultimo elemento, mas se vc passar um índice como posição ele chuta esse item pra fora da lista
print(f'Lista de lanches = {lanche}')   #por conta disso ele ra utilizado em listas, porque dessa forma vc da 'append' em um novo item no topo da lista e depois da 'pop' no mesmo ultimo item da lista
del lanche[3]
print(f'Lista de lanches = {lanche}')
print('\n')
print('Utilizando o método ".remove(item)" ')
print('lanche.remove("hamburguer")')
print(f'Lista de lanches = {lanche}')
lanche.remove('hamburguer')                 #Esse método procura na lista o primeiro índice que tem esse mesmo conteúdo, e dessa forma remove ele... é bom usar quando não se sabe exatamente onde está na lista
print(f'Lista de lanches = {lanche}')       #ou quando se quer verificar se tem esse determinado item e quer remove-lo
print('\n')
#lanche.remove(3) #se você tentar remover um item que não tem na lista vai dar erro, e te avisar que esse item não consta la lista, então use tratamento de erros para não quebrar seu código (ValueError: list.remove(x): x not in list)

print('---Criando listas com o "range()"')
print('Lista chamada "valores" que vai guardar números indo de 4 até 11')
print('O "list(range(inicio, fim))" é semelhante ao "for" e desconsida o item do fim')
print('valores = list(range(4,11))')
valores = list(range(4,11))
print(valores)
print('\n')
valores = [8,2,5,4,9,3,0]
print('Lista original: ',end='-> ')
print(f'valores = {valores}')
valores.sort() #através desse método você pode fazer com que a lista se torne ordenada
print('Lista ordenada: ',end='-> ')
print(f'valores = {valores}')
print('Lista Ordenada ao INVERSO: ',end='-> ')
valores.sort(reverse= True) #Essa forma como parâmetro 'Reverse' torna a lista ordenada de trás para frente
print(f'valores = {valores}')
print('O comando len("nome_da_lista") retorna o tamanho da lista')
print(f'valores = {len(valores)}')

#parte prática da aula

num = [2,5,9,1]
print(num)
num.append(7)
print(num)
num.sort()
print(num)
num.sort(reverse=True)
print(num)
print(f"ESSA LISTA TEM TANTOS ELEMENTOS = {len(num)}")
num.insert(2,0)
print(num)
num.pop()
print(num)
num.pop(2)
print(num)
num.insert(2,2)
print(num)
num.remove(2)
print(num)
if 4 in num:
    num.remove(4)
else:
    print('Não achei o n=4 para remover')

valores = []
valores.append(5)
valores.append(9)
valores.append(4)
print(valores)
for v in valores:
    print(f'{v}...',end='')
for indice, valor in enumerate(valores):
    print(f'Na posição {indice} valor = {valor}...',end='')
print('Final da lista')
#valores = []
#for cont in range(0,5):
#    valores.append(int(input('Entre com um valor: ')))
#for indice, valor in enumerate(valores):
#    print(f'Na posição {indice} tem o conteúdo {valor}...',end='')
#print('fim das entradas')

a = [2,3,4,7]
b = a
print(a)
print(b)
b[2] = 8
print(a)
print(b)
b = a[:]
b[2] = 4
print(a)
print(b)