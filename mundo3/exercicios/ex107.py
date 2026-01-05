#Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). 
# Faça também um programa que importe esse módulo e use algumas dessas funções.
from moeda import transformacao
entrada = float(input('Entre com algum valor em R$: '))
taxa = float(input('Entre com a taxa: '))
print(transformacao.moeda(entrada))

print('\nResolução do professor!')
aumentar = transformacao.aumentar(entrada,taxa)
print(f'[AUMENTAR] O preço {entrada}  mais a taxa de {taxa} é igual a [{aumentar}]')
diminuir = transformacao.diminuir(entrada,taxa)
print(f'[DIMINUIR] O preço {entrada} menos a taxa de {taxa} é igual a [{diminuir}]')
dobro = transformacao.dobro(entrada)
print(f'[DOBRO] O dobro do preço {entrada} é [{dobro}] ')
metade = transformacao.metade(entrada)
print(f'[METADE] A metrade do preço {entrada} é [{metade}]')