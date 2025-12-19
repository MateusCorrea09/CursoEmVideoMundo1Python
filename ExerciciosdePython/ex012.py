#faça um algoritmo que leia o preço de um produto e mostre seu novo
#preço com 5% de desconto

entrada_preco = float(input('Entre com o valor do produto: R$ '))
desconto = (entrada_preco * 5) / 100
preco_final = entrada_preco - desconto 
print('O preço do produto clculando 5% de desconto é de R$[{:.2f}]'.format(preco_final))