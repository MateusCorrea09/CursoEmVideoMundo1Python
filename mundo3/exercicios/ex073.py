#Crie uma tupla preenchida com 20 primeiros colocados da tabela do campeonato brasileiro de Futebol
# na ordem de colcoação. deposi mostre:
# Apenas os 5 primrios colocados.
# os últimos 4 colocados da tabela
# uma lista com os times em ordem alfabética
# Em que posição na tabela está o time da chapecoense

tabela = ('Athletico-PR','Atlético-MG','Bahia,Botafogo','Bragantino','Chapecoense','Corinthians','Coritiba','Cruzeiro','Flamengo','Fluminense','Grêmio','Internacional','Mirassol','Palmeiras','Remo','Santos','São Paulo','Vasco','Vitória')
#print(len(tabela)) #descobri que a tabela tem 29 itens
print(f'Os 5 primerios colocados são {tabela[:5]}')
print(f'os 4 ultimos colocados são {tabela[15:]}')
print('Os times em ordem alfabética são organizados da seguinte forma:')
for i in sorted(tabela):
    print(i)
print('A posição da chapecoense na tabela é : ',end= '')
posicao = tabela.index('Chapecoense') + 1
print(posicao)