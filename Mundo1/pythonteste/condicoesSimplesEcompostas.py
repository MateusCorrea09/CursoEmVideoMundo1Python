#trabalhar com possibilidades ou desvios de percurso
#'todo programa possui diversas estruturas condicionais'
#para construir a estrutura condicional precisamos usar a identação (que seria a forma de escrita)
#if 'condição':
#   oque aocntece() // se True
#elif condicão_secundaria:
#   oque acontece() // se True
#else:
#   se tudo der errado_faz isso()   //Se False
#if = 'se', else = 'se não'

tempo = 4 #tempo de uso do carro
print('--- teste de aplicação if/else')
if tempo <= 3:  #Se True
    print('Carro novo!')
else:           #Se False
    print('Carro velho :D')
print('---Fim da aplicação---')

#Condição simplificada, que é quando usamos poucas linhas para simplificar uma estrutura condicional
#o professor chamou isso de operador Ternario ou Termario, não cheguei a ver isso nas outras linguagens
tempo = 4 #tempo de uso do carro
print('--- teste de aplicação if/else')
print('Caro novo!' if tempo <= 3 else 'Carro velho :D')
print('---Fim da aplicação---')

#Verificação de String
nome = 'Marcos'
if nome == 'Gustavo':# a estrutura abaixo só acontece caso retornar um True na checagem... se o nome for igual a Gustavo
    print('que nome lindo você tem!')
else: # SE A CHECAGEM RETORNAR FALSE
    print('Seu nome é normal :D')
print('bom dia {}!'.format(nome)) # o print de bom dia sempre vai acontecer

#Teste de média
n1 = 7.5
n2 = 6.5
m = (n1+n2)/2
print('Sua média é [{}]'.format(m))
if m >= 6:
    print('Sua média foi boa!')
else:
    print('Sua média não foi boa, estude mais!')
print('PARABÉNS!' if m == 10 else 'você pode estudar um pocuo mais!')
