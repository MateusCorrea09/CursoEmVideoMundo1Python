#Crie um programa que leia o nome e o preço de vários produtor. O programa
# devera perguntar se o usuário vaio continuar e no final, mostre?:
# qual é o total de dastos na compra
# quantos produtos custam mais de 100 reais
# qual é o nome do produto mais barato
total_gasto = 0
quant_produto_caro = 0
produto_acessivel = 0
nome_produto_acessivel = ''
cont = 1
while True:
    produto = str(input('Entre com o nome de um produto: '))
    preco_produto = float(input('Entre com o preço do produto: '))
    total_gasto += preco_produto
    if preco_produto > 1000:
        quant_produto_caro += 1
    if cont == 1:
        produto_acessivel = preco_produto
    else:
        if preco_produto < produto_acessivel:
            produto_acessivel = preco_produto
            nome_produto_acessivel = produto
    resposta = str(input('Você deseja continuar [S / N ]?: ')).upper()
    if resposta == 'N':
        break
    cont += 1
print('O nome do produto mais acessivel é [{}]'.format(nome_produto_acessivel))
print('O total de gastos é de R$[{:.2f}]'.format(total_gasto))
print('A quantidade de produtos caros com valor +de R$1000 é de [{}]'.format(quant_produto_caro))