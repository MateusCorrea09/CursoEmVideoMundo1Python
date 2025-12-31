# é possível declarar uma listas de duas formas:
dados = list() #ou
dados.append('Pedro')
print(dados) 
#Ambos foram criados e funcionaram para criar a lista 'dados'
dados.append(25)
#Hoje vamos ver listas dentro de listas, que seriam as matrizes
#pessoas = list()
#pessoas.append(dados[:]) #é tipo juntar as listas dentro de outra
pessoas = [['pedro',25],['Maria', 19],['João',32]]
print('---Printando um linha coluna---')
print(pessoas[0][0])#print Pedro
print(pessoas[1][1])#print 19
print(pessoas[2][0])#print João
print('---Printando todo um índice da lista principal---')
#isso significa que será printado todo conteúdo dentro de um índice da matriz
print(pessoas[1])# então o programa vai no índice 1 da 'Lista' pessoas... e vai printar tudo oq tem lá
"""print('\n')
print('---Parte prática da aula---')
#Parte prática
teste = list()
teste.append('Gustavo')
teste.append(40)
print('--Criando uma lista chamada "teste"')
print(teste)
galera = list()
galera.append(teste)
print('--Nova lista "galera"--\n lista "Teste" dentro de "Galera"')
print(galera)
print('--Exemplo de como a ligação entre listas pode gerar um problema de leitura--')
#Isso significa que ao mudar a lista teste pode gerar dados duplicados e repetidos
#o correto é usar uma cópia, não uma associação '[:]'
teste[0] = 'maria'
teste[1] = 22
galera.append(teste)
print(galera)"""
print('\n')
print('---Parte prática da aula---')
#Parte prática
teste = list()
teste.append('Gustavo')
teste.append(40)
print('--Criando uma lista chamada "teste"')
print(teste)
galera = list()
galera.append(teste[:])
print('--Nova lista "galera"--\n lista "Teste" dentro de "Galera"')
print(galera)
teste[0] = 'maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
print('--Declarando galera de novo--')
galera = [['João',19],['Ana',33],['Joaquim',13],['Maria',13]]
print(galera)
print('Printando todo o conteúdo dento do índice 0')
print(galera[0])
print('Printando um conteúdo específico dento de galera')
print(galera[0][0])
print('Printando cada índice de galera usando um loop "for"')
for p in galera:
    print(p) 
print('--Printando apenas os nomoes / que seriam os primeiros índices dentro de cada lista interna--')
for p in galera:
    print(p[0]) 
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade') #isso serve para quando sabemos oq tem
                                              #em cada lista interna... e quando elas estão já organizadas
galera.clear()
dados.clear()

print('\n--Entrando com dados dentro de uma matriz--')
galera = list() #Essa vai ser a lista que vai ser armazenada os dados
dado = list() #Essa é a lista auxiliar que vai armazenar os dados de forma temporária em cada ciclo do loop
for conteúdo in range(0,3):
    dado.append(str(input('Entre com seu nome: ')))
    dado.append(int(input('Entre com sua idade: ')))
    galera.append(dado[:]) #importante lembrar de coloca o '[:] de cópia'
    dado.clear() #Isso é para garantir que oq está dentro de 'dado' seja excluído, desas forma ficará pronto para
                 #o próximo loop
print(galera)
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
    else:
        print(f'{p[0]} é menor de idade')
