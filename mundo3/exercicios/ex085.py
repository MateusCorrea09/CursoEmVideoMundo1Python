#Crie um programa onde o usuário possa digitar sete 
# valores numéricos e cadastre-os em uma lista única
# que mantenha separados os valores pares e ímpares 
# No final mosre os valores ímpares em ordem crescente

numeros_pares = list()
numeros_impares = list()

for i in range(0,6):
    numero_entrada= int(input('Entre com um valor: '))
    if numero_entrada %2 == 0:
        numeros_pares.append(numero_entrada)
    else:
        numeros_impares.append(numero_entrada)
numeros_pares.sort()
numeros_impares.sort()
print(f'Os numeros pares são [{numeros_pares}]')
print(f'Os numeros ímpares são [{numeros_impares}]')