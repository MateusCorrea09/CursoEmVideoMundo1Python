#CRIE UM PROGRAMA QUE LEIA A BASE E ALTURA E DEVOLVA O TAMANNHO EM M2 DA PAREDE DE UMA CASA
#E TAMBÉM DIGA QUANTAS LATAS DE TINTA SÃO NECESSÁRIAS PARA QUE ESSA PAREDE SEJA PINTADA, CONSIDERE
#QUE A CADA 2 METROS2 DE PAREDE SÃO USADAS 1 LATA DE TINTA
entrada_base = float(input('Largura da parede: '))
entrada_altura = float(input('Altura da parede: '))
area = entrada_base * entrada_altura
latas_tinta = area / 2

print('sua parede tem :[{}]x[{}] de dimensão e a área é de [{}]m2'.format(entrada_base,entrada_altura,area))
print('para pintar a sua parede são necessárias [{:.2f}] latas de tinta'.format(latas_tinta))