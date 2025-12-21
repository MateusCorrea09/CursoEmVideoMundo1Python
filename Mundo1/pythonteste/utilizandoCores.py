#utilizando o padrão ANSI usamos primeiro '\033' + '[' + um número para o estilo + um número para o texto + um número para o back ground + 'm'
#os números para Style que funcionam melhor no python para o terminal são 0, 1, 4 e 7
#as cores para texto são 30, 31, 32, 33, 34, 35 e 37
# o background 40, 41, 42, 43, 44, 45, 46 e 47
#\033[0;30;41m
#\033[4;33;44m
#\033[1;35;43m
#\033[30;42m
#\033[m
#\033[7;30m
print('Olá mundo!')
print('\033[31mOlá mundo!\033[m') # em vermelho
print('\033[1;31;43mOlá mundo!\033[m') # em vermelho com fundo amarelo
print('\033[4;30;45mOlá mundo!\033[m')
print('\033[7;30mOlá mundo!\033[m')

#utilizando cores para printar resultados na tela
a = 3
b = 5
print('Os valores são \033[32m[{}]\033[m e \033[31m[{}]'.format(a,b))

nome = 'Marcos'
# estrutura organizacional de cores {cor} + {variavel} + {código de fechamento da cor}
print('O lá muito prazer em te conhecer {}[{}]{}!'.format('\033[4;34m', nome,'\033[32m'))