#Faça um programa que tenha uma função chamada área(), que receba as dimensões de um
# terreno retangular (largura e comprimento) e mostre a área do terreno.

def retorna_area(x,y):
    print(f' O resultado da área do terreno com base = [{x}] e altura [{y}] é [{x * y}]')
def quebra_linha():
    print('==='*30)
quebra_linha()
retorna_area(2,4)
quebra_linha()
retorna_area(4,7)
quebra_linha()
retorna_area(8,9)
quebra_linha()


