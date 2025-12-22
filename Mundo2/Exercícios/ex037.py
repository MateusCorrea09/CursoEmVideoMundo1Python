#escreva um programa que leia m número inteiro qualquer e peça para
#o usuário escolher qual será a base de conversão
#1 para binário (0 1)
#2 para octal (8)
#3 para hexadecimal (16)
numero = int(input('Entre com um número inteiro: '))
numero_entrada = numero
#print('[{}]'.format(bin(numero)))
#1 \\ 2 \\ 4\\\ 8 \\ 16 \\32 \\64 \\128 \\256 \\512 \\1024
#print('[1024]||[512]||[256]||[128]||[64]||[32]||[16]||[8 ]||[4 ]||[2 ]||[ 1]||')
#print('[ {} ]||[ {}]||[{} ]||[{} ]||[{}]||[{}]||[{}]||[{}]||[{}]||[{}]||[{}]||'.format(numero % 1024,numero%512,
#                                                                                       numero % 256,numero % 128,
#                                                                                       numero % 64, numero %32,
#                                                                                       numero % 16, numero % 8,
#                                                                                       numero % 8, numero %4,
#                                                                                       numero % 2, numero %1))
#tentei fazer uma coisa :D
escolha = int(input('Entre com uma das alternativas abaixo: \n 1 - Binário\n 2 - Octal\n 3 - Hexadecimal\n'))
if escolha == 1:
    if numero >= 1024:
        numero = numero % 1024
        primeira_casa = 1
    elif numero < 1024:
        primeira_casa = 0
    if numero >= 512:
        numero = numero % 512
        segunda_casa = 1
    elif numero < 512:
        segunda_casa = 0
    if numero >= 256:
        numero = numero % 256
        terceira_casa = 1
    elif numero < 256:
        terceira_casa = 0
    if numero >= 128:
        numero = numero % 128
        quarta_casa = 1
    elif numero < 128:
        quarta_casa = 0
    if numero >= 64:
        numero = numero % 64
        quinta_casa = 1
    elif numero < 64:
        quinta_casa = 0
    if numero >= 32:
        numero = numero % 32
        sexta_casa = 1
    elif numero < 32:
        sexta_casa = 0
    if numero >= 16:
        numero = numero % 16
        setima_casa = 1
    elif numero < 16:
        setima_casa = 0
    if numero >= 8:
        numero = numero % 8
        oitava_casa = 1
    elif numero < 8:
        oitava_casa = 0
    if numero >= 4:
        numero = numero % 4
        nona_casa = 1
    elif numero < 4:
        nona_casa = 0
    if numero >= 2:
        numero = numero % 2
        decima_casa = 1
    elif numero < 2:
        decima_casa = 0
    if numero == 1:
        decimaprimeira_Casa = 1
    if numero == 0:
        decimaprimeira_Casa = 0
    print('{}||{}||{}||{}||{}||{}||{}||{}||{}||{}||{}||'.format(primeira_casa,segunda_casa,
                                                                                       terceira_casa,quarta_casa,
                                                                                       quinta_casa, sexta_casa,
                                                                                       setima_casa, oitava_casa,
                                                                                       nona_casa, decima_casa,
                                                                                       decimaprimeira_Casa))
    #no caso jpa existe formas melhores de fazer isso em python... :D descobri isso na aula do professor
    print('O valor [{}] convertido para binário é [{}]'.format(numero_entrada,bin(numero_entrada)[2:]))
elif escolha == 2:
    print('O valor [{}] convertido para octal é [{}]'.format(numero, oct(numero)[2:]))
elif escolha == 3:
    print('O valor [{}] convertido para hexadecimal é [{}]'.format(numero,hex(numero)[2:]))
else:
    print('Entre com uma alternativa válida!')

