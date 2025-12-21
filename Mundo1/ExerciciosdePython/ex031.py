#Desenvolva um programa que pergunte a distância de uma viagem em KM.
#Calcule o preço da passagem, cobrando R$0,50 por cada km para viagens
# de até 200Km e R$0,45 para viagens mais longas.
import emoji
distancia = float(input('🚌Entre com a distândia da viajem🚌'))
if distancia <= 200:
    distancia = distancia * 0.50
    print('O valor a ser cobrado pela viajem é de R$[{}] 💸'.format(distancia))
else:
    distancia = distancia * 0.45
    print('O valor a ser cobrado pela viajem é de R$[{}] 💸'.format(distancia))