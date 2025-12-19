#na matemática usamos sinais para atribuir sooma, multiplicação, divisão subtração e ente outras contas matemáticas
# na matemática tem outras coiasa possibilidades como encontrar o resto de uma divisão
# em python e em outras linguagens, usamos os operando + um operador artmimético + outro opeando
#ex soma = operando1 + operando2. nesse exemplo soma receberá a soma de dois operando por meio do operador artimético '+'
print(5 + 2) #soma, resultado esperado 7
print(5 -2) #subtração, resultado esperado 3
print(5 * 2) #Multiplicação, resultado esperado 10
print(5 / 2) #divisão, resultado esperado 2.5
print(5 ** 2) #potenciação, resultado esperado 25
print(5 // 2) # divisão com resto inteiro, resultado esperado 2 (ele sempre arredonda para inteiro, e para BAIXO)
print(5 % 2) #resto da divisão, resultado esperado 1 (2 * 2 =4 ... resta 1 para chegar no '5')
 ## os '==' significa "Igual" é pra retornar um True ou False, caso seja verdade, exemplo:
print(5 * 2 == 9) # o resultado é 'False' porque não é '9' o resultado e sim '10'
 ## os '!=' significa 'diferente'
print(5 * 2 != 9) # o resultado é "True" porque de fato o resutlado é '10' não '9'

## ordem de precedência
#1º lugar o '( )'
#2º lugar o '**'
#3º lugar o '*','/','//','%'
#4º lugar o '+' e '-'
#' Fazer um programa e ele funcionar não necessáriamente quer dizer que ele esta certo, e sim pode estar dando erro
# por conta da organização errada de ordem de precedência- Guanabara'

##exercício em aula
##ordem de precedência:
#qual é a saída desse código '5 + 3 * 2'
# resposta: primeiro eu devo resolver a multiplicação e depois a soma... logo 3 * 2 = 6 ... 5 + 6 = '11'

#'3 * 5 + 4 ** 2'
#resposta: 4 ** 2 = 16 ... 3 * 5 = 15 ....15 + 16 = '31'

# '3 *( 5 + 4 )** 2'
#resposta: 5 + 4 = 9 ... 9 ** 2 = 81 ... 81 * 3 = '243'

#exercícios propóstos:
#existe algumas derramentas que eprmitem modificar a forma com que as coisas podems er exibidas para um usuário.
#no caso do print podemos usar uma formatação e exibir um determinado numero de caracters uma certa quantia de vezes.
nome = 'Mateus' #eu posso fazer ele ter por 20 caracteres
print('prazer em te conhecer {:20}![ponto de final]'.format(nome))# nesse caso o '!' ficará um pocon longe... porque ele
                                                                  #adicionando 'espaço' até dar '20' caracteres
print('prazer em te conhecer {:>20}![ponto de final]'.format(nome))# adicionando o '>' eu digo que eu quero que ele seja
                                                                    # no final, depois dos espaços complementares
print('prazer em te conhecer {:^20}![ponto de final]'.format(nome))#agora dessa forma usando o '^' ele será alinhado ao meio
print('prazer em te conhecer {:=^20}![ponto de final]'.format(nome))# dessa forma será exibido centralizado com '=' no lugar dos espaçoes
#o print tem muitas utlixadas, pode dar uma olhada a mais em cada possibilidade

n1 = int(input('entre com um valor: '))
n2 = int(input('entre com outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('a soma vale [{}], o produto é [{}] e a divisão é [{}]'.format(s,m,d))
print('divisão inteira [{}] e portência [{}]'.format(di,e))
print('O resultado da divisão formatada é [{:.3}]'.format(d)) #para formatar um valor usamos ' :.3 ' dentro do '{}'
#no python podemos evitar a quebra de linha substituindo ela por '' (nada)... isso se dpa por meio de uma informação
#que pode estar oculta quando estamos vendo da forma que doi apresentada até então... no sentido de que existe uma informação
#no print que não estavamos vendo,q ue seria o ' end = '\n' ' isso significa que a todo final de 'print()' o 'end' considera uma quebra de linha
#podemos mudar isso tirando o '\n' que está sendo apssado como argumento..
print('a soma vale [{}], o produto é [{}] e a divisão é [{}]'.format(s,m,d), end = '') #observe que aki eu usei um ',' e depois passei como argumento dentro do 'end' o [''] que seria o nada ou vazio
print('divisão inteira [{}] e portência [{}]'.format(di,e))                            #dessa forma a linha não é quebrada

#fAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E MOSTRE NA TELA SEU SUCESSOR E SEU ANTECESSOR
entrada1 = int(input('Entre com um número: '))
print('o antecessor de {} é {} e o sucessor é {}'.format(entrada1,entrada1 - 1, entrada1 + 1))

#Crie um algoritmo que leia um numero e mostre o seu dobro o seu triplo e a raiz quadrada
print('o dobro de [{}] é [{}] !'.format(entrada1, entrada1 * 2))
print('o triplo é: [{}]'.format(entrada1 * 3))
#print('A raiz quadrada de [{}] é [{}] !'.format(pow(entrada1, 0.5)))

#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a média
nota1 = 8.3
nota2 = 9.2
nota3 = 5.5
media = (nota1 + nota2 + nota3) / 3
print('A média do aluno é: [{:.3}]'.format(media))