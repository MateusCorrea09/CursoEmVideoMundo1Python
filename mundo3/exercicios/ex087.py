# Aprimore o desafio anterior, mostrando no final
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# O maior valor da segunda linha.
matriz = [[0,0,0],[0,0,0],[0,0,0]]
total_pares = 0
soma_terceiracoluna = 0
for i in range(0,3):
    for j in range(0,3):
        matriz[i][j] = int(input(f'Entre com um valor [{i}][{j}]: '))
        if matriz[i][j] % 2 == 0:
            total_pares += matriz[i][j]
maior_segunda_linha = matriz[1][0]
for i in range(0,3):
    for j in range(0,3):
        print(f'[{matriz[i][j]}]',end='')
        if j == 2:
            soma_terceiracoluna += matriz[i][j]
        if i == 1:
            if maior_segunda_linha < matriz[i][j]:
                maior_segunda_linha = matriz[i][j]
    print()
print(f'A soma de todos os valores pares é [{total_pares}]')
print(f'O maior numero da segunda linha é [{maior_segunda_linha}]')
print(f'A soma de todos os valores da terceira coluna é [{soma_terceiracoluna}]')

