#Dicionarios nos dão a possibilidade de trabalhar com índices 'literais' ao invés de númericos como
# são utilizadas nas listas.
# Dicionários são estruturas de dados que possibilitam ter índices literais
# um diciionario é reconhecido pelo uso de '{}'
dados = dict()
dados = {'nome':'Pedro', 'idade':25}
print(dados)
print('Atribuindo um novo índice a estrutura dicionário "dados"')
dados['sexo'] = 'M'
print(dados)
print('Removendo um índice do dicionario através do comando "del"')
del dados['idade'] # ele recomve o índice e a estrutura se reorganiza 
print(dados)
print('\n')

print('Criando um novo dicionário')
filme = {'titulo':'StarWars',
         'ano':1977,
         'diretor':'George Lucas'
        }
print(filme)
print('Acessando todos os valores do dicionário, que seria oq tem guardado dentro dos índices')
print(filme.values())
print('Acessando os índices/keys')
print(filme.keys())#retorna os literais dos índices
print('Acessando ambos os conteúdos')
print(filme.items())
print('\n')
#é possível usar essa relação entre keys e itens para utlizar em estruturas de repetição
for key, value in filme.items(): #A 'key' é o titulo/indice/literal o 'value' é o conteúdo do índice
    print(f'O {key} é {value}')
print('\n')
filme1 = dict()
filme2 = dict()
filme1['titulo'] = 'avengers'
filme2['titulo'] = 'matrix'
filme1['ano'] = 2012
filme2['ano'] = 1999
filme1['diretor'] = 'joss Whedon'
filme2['diretor'] = 'wachowski'
print('Criando novos dicionários')
print(f'Filme 0 : {filme}')
print(f'Filme 1 : {filme1}')
print(f'Filme 2 : {filme2}\n')
print('Adicionando dicionarios em índices de "Listas"')
locadora = list()
locadora=[filme,filme1,filme2]
print(f'Printando todo o conteúdo dentro da lista "Locadora"\n{locadora}')
print('printando um conteúdo esécifico dentro de locadora, a partir do seu [índice][key]\n')
print(f'[[locadora[0]["titulo"]] -> {locadora[0]['titulo']}')
print(f'[[locadora[1]["titulo"]] -> {locadora[1]['titulo']}')
print(f'[[locadora[2]["titulo"]] -> {locadora[2]['titulo']}')

print('\n---Parte prática da aula!---\n')
pessoas = {'nome': 'Gustavo', 'sexo': 'M','idade': 22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')# vc tem que ter atenção com as aspas, pois
        #se vc começa a fazer um print com aspas simples, vc deve usar aspas duplas dentro das chaves, isso
        #evita erro.

print('-'*30)
print('printando coisas específicas do dicinário')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k in pessoas.keys():
    print(k)
for k,v in pessoas.items():
    print(f'{k} = {v}')
print('-'*30)
print('Atualizando o conteúdo dentro do dicionário\n usando o "pessoas["key"] = "novo conteúdo""')
pessoas['nome'] = 'Leandro'
for k,v in pessoas.items():
    print(f'{k} = {v}')

print('-'*30)
print('adicionando um novo item ao dicionário\n usando o pessoas["novo item"] = "conteúdo novo item"')
pessoas['peso'] = 98.5 # não é preciso usar append
for k, v in pessoas.items():
    print(f'{k} = {v}')

print('-'*30)
print('Criando um novo dicionário')
brasil = list()
estado1 = {'uf' : 'Rio de janeiro', 'sigla' : 'RJ'}
estado2 = {'uf' : 'São Paulo' , 'sigla' : 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0])
print(brasil[1])
print(brasil[0]['uf'])
print(brasil[1]['sigla'])
print('-'*30)
print('Vamos fazer um pequeno loop parae receber duas informações e armazena-las em um dicionario')
print('E depois usar o método interno do dicionário para realizar uma "Cópia" do dicionario para uma lista')
estados = dict()
brasil= list()
for c in range(0,3):
    estados['uf'] = str(input('Unidade Federativa: '))
    estados['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estados.copy())
    #usamos o 'copy()' para copiar um conteúdo dentro de um dicionário para outro lugar
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}') 