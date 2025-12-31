#Crie um programa que cie uma matriz de dimensão 3x3 e preencha com valores
#lidos pelo teclado
#No final, mostre a matrz na tela com a formação correta
#print('[] [] []\n[] [] []\n[] [] []')
matriz = [[0,0,0],[0,0,0],[0,0,0]]
for i in range (0,3):
    for j in range(0,3):
        matriz[i][j] = int(input(f'[{i}]:[{j}]: '))
print(matriz)
for i in range (0,3):
    for j in range(0,3):
        print(f'[{matriz[i][j]}]', end='')
    print('')