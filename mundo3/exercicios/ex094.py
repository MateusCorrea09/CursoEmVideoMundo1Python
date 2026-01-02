# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada 
# pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
#  A) Quantas pessoas foram cadastradas
#  B) A média de idade
#  C) Uma lista com as mulheres D)
#  Uma lista de pessoas com idade acima da média
registros = list()
pessoa = dict()
cont_cadastros = media_idade = cont_acima_da_media = 0
mulheres_cadastradas = list()
pessoas_media_idade = list()
while True:
    pessoa['nome'] = str(input('Entre com seu nome: '))
    pessoa['sexo'] = str(input('Entre com seu gênero [M ou F]: ')).lower()
    #tem que salvar numa lista se o usuário pertencer ao gênero feminino
    pessoa['idade'] = int(input('Entre com sua idade: '))
    media_idade += + pessoa['idade']
    registros.append(pessoa.copy())
    cont_cadastros += 1
    #print(cont_cadastros)
    if pessoa['sexo'] == 'f':
        mulheres_cadastradas.append(pessoa.copy())
    pessoa.clear()
    resp = str(input('Registro finalizado com sucesso!\n   Deseja continuar [S / N] ?')).lower()
    if resp == 'n':
        break

media = media_idade / cont_cadastros
'''isso abaixo esta verificando dentro de um dicionario vazio, por isso n ta retornando as informações corretas'''
'''for key, value in pessoa.items():
    if key == 'idade':
        if value > media:
            cont_acima_da_media += 1
            pessoas_media_idade.append(pessoa.copy())'''
#olhei minhas anotações e achei essa de como acessar um dicionário dentro de uma lista, está nas anotações da aula 'dicionario.py'
#uma coisa bem especifica srsr e pode causar confusão porque se vc olhar em 'i.items()' o 'items()' esta branco e parece que ta errado
for i in registros:
    for key, value in i.items():
        if key == 'idade' and value > media:
            pessoas_media_idade.append(i.copy())
    
if key == 'idade' and value > media:
    pessoas_media_idade.append(pessoa.copy())
            
print('-'*30)
for i in pessoas_media_idade:
    for key, value in i.items():
        print(f'{key} tem valor {value}')
print('-'*30)
print(f'A media de idade é [{media}] e o número de pessoas com a idade superior a média é [{cont_acima_da_media}]')
print('-'*30)
for i,conteudo in enumerate(registros):
    print(f'Registro [{i + 1}][{conteudo}]')
print('-'*30)
print(f'Mulheres cadastradas [{len(mulheres_cadastradas)}]')
for i, conteudo in enumerate(mulheres_cadastradas):
    print(f'Registro [{i + 1}] [{conteudo}]')