#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#à vista dinheiro/cheque: 10% de desconto
#à vista no cartão: 5% de desconto
#em até 2x no cartão: preço formal 
#3x ou mais no cartão: 20% de juros
valor_produto = float(input('Entre com o valor a ser pago pelo produto: '))
escolha = int(input('escolha dentre as alternativas abaixo:\n1 - Á vista dinheiro/cheque: 10% de desconto\n2 - à vista no cartão: 5% de desconto' \
'\n3 - Em até 2x no cartão: preço formal \n4 - 3x ou mais no cartão: 20% de juros'))
if escolha == 1:
    desconto = (valor_produto * 10) / 100
    preco_final = valor_produto - desconto
    print('O valor final da compra é de [R${:.2f}] com o desconto de 10% no valor de [R${:.2f}]'.format(preco_final,desconto))
elif escolha == 2:
    desconto = (valor_produto * 5) / 100
    preco_final = valor_produto - desconto
    print('O valor final da compra é de [R${:.2f}] com o desconto de 5% no valor de [R${:.2f}]'.format(preco_final,desconto))
elif escolha == 3:
    print('O valor final do produto é de [R${:.2f}], pois não há desconto aplicavel'.format(valor_produto))
elif escolha == 4:
    juros = (valor_produto * 20) / 100
    preco_final = valor_produto + juros
    print('O valor final do produto é de [R${:.2f}], por conta de um jutos de 20% aplicado [R${:.2f}]!'.format(preco_final,juros))
else:
    print('Erro!')