
entrada = str(input('Entre com uma frase: ')).strip().upper()
print('Cê digitou a frase [{}]'.format(entrada))
palavras = entrada.split()
junto = ''.join(palavras)
inverso =''
for letra in range (len(junto) - 1, -1, -1):
    inverso +=junto[letra]
if inverso == junto:
    print(inverso)
    print('É um padíndromo')
else:
    print('A frase não é um palíndromo')