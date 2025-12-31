#  Faça um programa que leia nome e peso de várias pessoas
# guardando tudo em uma lista. No final mostre:
# quantas pessoas foram cadastradas
# uma listagem com as pessoas mais pesadas
# uma listagem com as pessoas mais leves
# segundo o professor 70 kg pessoas leves 100kg pessoas pesadas
cont_pessoas_cadastradas = 0
pessoas_pesadas = list()
pessoas_leves = list() #vai armazenar nome e peso
dados_entrada = list()
while True:
    dados_entrada.append(str(input('Entre com seu nome: ')))
    dados_entrada.append(float(input('Entre com seu peso: ')))
    cont_pessoas_cadastradas += 1
    if dados_entrada[1] <= 70:
        pessoas_leves.append(dados_entrada[:])
        
    if dados_entrada[1] >= 100:
        pessoas_pesadas.append(dados_entrada[:])
        
    dados_entrada.clear()
    resp = str(input('Deseja continuar [s / n]?: ')).lower()
    if resp == 'n':
        break
print(f'A quantidade de pessoas cadastradas é {cont_pessoas_cadastradas}')
print('As pessoas mais pesadas são:')
for i in pessoas_pesadas:
    print(f'Nome: {i[0]} e tem {i[1]} KG')
print('\nAs pessoas mais leves são:')
for i in pessoas_leves:
    print(f'Nome {i[0]} e tem {i[1]} KG')
print('Fim da aplicação :D')