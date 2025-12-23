#desenvolva um programa que leia o primeiro termo e a razão de um PA. no final
#mostre os 10 primeiros termos dessa progressão
#vídeo que me salvou 'https://www.youtube.com/watch?v=poyvpdAC4xI'
entrada = int(input('Entre com o primeiro termo: '))
entrada_razao = int(input('Entre com a razão da PA: '))
soma_total = entrada
for i in range(1,11):
    conteudo = entrada + (i - 1) * entrada_razao
    print('[A{}] = [{}]'.format(i,conteudo))    

###
#O professor usou uma ferramenta de print que eua chei legal
print('\nSolução de print de tela alternativa, proposta pelo professor:')
decimo = entrada + (10 -1) * entrada_razao
for c in range(entrada, decimo + entrada_razao, entrada_razao):
    print('[{}]'.format(c), end='-> ') #gostei que ele usou o 'end' para indicar a proxima coisa a aparecer na tela!
print('Fim')
