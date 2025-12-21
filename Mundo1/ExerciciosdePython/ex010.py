#Crie um algoritmo que pegue o quanto a pessoa tem de dinheiro na carteira
# e converta para quantos dolares isso vale, levando em consideração que 
#o dolar está a R$ 3.27

entrada = float(input('entre com o seu valor disponível na sua carteira: R$'))
print('O valor convertido em dolar(s) é de US$[{:.2f}]'.format(entrada / 3.27))