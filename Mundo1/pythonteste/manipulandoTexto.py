#cadeias de texto em python ou em outras linguagens são chamadas de Strings
#exemplo nome = 'Mateus de Jesus Corrêa' é uma string
frase = 'curso em vídeo python'
# o que o computador faz é pegar cada caracter e posicionali em um espaço delimitado na memória
#é como se imaginarmos que a frase comtem 15 caracteres, então o computador pega um espaço na memória e o divide em 15 pedaços
#cada pedaço sera guardado um caracter dessa 'frase'
#cada espaço recebe um 'índice' [SIMILAR A VETORES no java, você acessa um vetor por meio de um endereço e índice]
#fatiamento é pegar uma string e fatiar ela em pedaços
#eu posso acessar uma determinada parte da string solicitando que seja acessada um determinado índice
print(frase[9]) #resultado esperado 'V'
#em pythom podemos comunicar a idéia de 'range' que significaria pro computador algo do tipo:
#'Olha computador... vái até esse índice e pega todas as partes até esse outro índice... mas esse final aki depois dos ':' não considera ele ok?'
#e para isso construímos dessa forma 'frase[9:13]' dessa forma ele vai pegar os conteúdos dÊs do índice 9 até o 12... desconsiderando o 13
print(frase[9:13]) #resultado esperado 'Víde'
print(frase[9:21]) #resultado esperado 'vídeo python'
# essa tipo de rescurso também possibilita a entrada de um terceiro argumento que se trata do 'ignorar' ou 'pular', um exemplo seria:
#resultado esperado 'vdopto'
#endereço[{início}:{fim}:{característica de ignorar ou pular}]
print(frase[9:21:2])# dessa forma ele vai printar apenas os conteúdos de 2 em 2... logo ele pula 2 índices logo após realizar um print na tela
#então seria um print pulando uma casa a opós a aoutra já que ela não conta o ultimo digito
print(frase[:5])#SERIA UM PRINTE TODOS OS ÍNDICES ATÉ O INDICE 4 E DESCONSIDERE O 5
#quando você omite o primeiro argumento você diz pro computador que ele deve começar a partir do índice inicial que seria '0'
print(frase[15:])#seria um printe todos os índices a partir do índice 15 e também o final
print(frase[9::3])#dessa forma ele vai printar todos os índices a partir do 9 e pulando de 3 em 3

#Existem algumas ferramentas úteis para lidar com uma string como realizar uma análise
#o método 'len()' retorna o tamanho dessa determinada string
print(len(frase))#retorna 20 pois a string tem 21 caracteres
#O método 'count()' ele conta quantos caracteres possuem dentro de ums string
print(frase.count('o')) #resultado esperado '3'
    #uma variação desse método é passar como argumento um inicio e fim de contagem (como um fatiamento), dessa forma ele contará em um determinado
    #range desconsiderando a ultiuma posição
print(frase.count('o',0,13)) #resultado esperado '1'
#Um outro método seria o 'find()' que seria 'encontrar' então ele printaria onde exatamente começa {o índice} a determinada sequência de carcteres
print(frase.find('deo'))
    #Esse mesmo método retorna '-1' caso ele não encontrar o argumento passado (é bom lembrar disso para não se assuatar quando retornar um índice -1)
print(frase.find('java')) #:D
#O OPERADOR 'in' pode ser usado apra retorno de TRUE ou FALSE a depender se existe ou não determinado conteúdo dentro da string
    #importante lembrar que esse Operador retorna não a posição... e sim o True ou False
print('curso' in frase)#resultado esperado True
print('java' in frase)#resultado esperado False

#Tranformação
#O método 'replace({argumento a ser procurado}, {argumento a ser colocado no lugar})' pega um determinado conteúdo dentro da string e se encontrado posiciona
#um outro no lugar
#pelo que eu entendi ele nao MUDA a string ... e sim só momentaneamente ??? ok então
print(frase.replace('python','Android'))
print(frase.replace('Android','Python:D')) # se ele não encontrar determinada parte ... ele só não faz nada mesmo... não da erro
#O método 'upper()' siginifica que ele deixa tudo em maiúsculo
print(frase.upper())# frase toda em maiúculos
print(frase) ## esse print serve para demosntrar como a string não é mudada eplo método
print(frase.lower())#esse método serve para deixar tudo em minusculo
print(frase)        #o mesmo vale para o 'lower()' ele não muda a string
#o método 'capitalize()' ele vai pegar toda a string e passar para minuscula e o primeiro caractere passa para maiúscula
print(frase.capitalize())
#O método 'title()' ele vai rpocurar todas as PALAVRAS dentro da string e colcoar todas as primeiras lestras em maiúscula... e o restante em minuscula
#ele vai usar os espaços como parâmetro de procura
print(frase.title())

#para ficar mais simples uma dterminada explicação vamos mudar  conteúdo dentro de 'frase'
frase ='   Aprenda Python  ' #perceba que estou colocando 'Espaços' adicionais dentro da string para facilitar uma esplicação sobre identificar entradas que contém espaços
# em uma determinada situação pode ser útil identificar espaços excessivos em uma entrada realizada pelo usuário
#então para isso usamos o método 'strip()' para remover os espaços no começo e no final da frase
print('A nova frase de entrada é: [{}]'.format(frase))
print('A frase sem os espaços no FINAL e no COMEÇO é: [{}]'.format(frase.strip()))
#da mesma forma que remover TODOS os espaçoes excessivos é útil, talves remover apenas de uma determinada direção seja o ideal para sua aplciação
#logo, podemos usar o 'rstrip()' para remover os da direita, o 'r' significa 'rigth' de 'direita' um termo em inglês
print('A frase sem os espaços da Direita é: [{}]'.format(frase.rstrip()))
#uma outra variação é usar o 'lstip()' para remover todos os da 'esquerda', o 'l' significa 'left' que seria um termo em inglÊs para 'esquerda'
print('A frase sem os espaços da Esquerda é: [{}]'.format(frase.lstrip()))

#Agora voltamos a string normal
frase = 'Curso em Vídeo Python'
# o método 'split()' vai pegar cada palavra dentro da string (e vai usar os espaçoes como parâmetro) e vai reoganizar par que cada
#paralavra seja uma string diferente ... as 'dividindo' em outras strings
#ele divide a string em outras strings formando uma lista... dessa forma você pode acessar uma determinada palavra a partir de um inteiro
print(frase.split())
print('-'.join(frase))# não entendi direito como isso funciona, acho que se torna melhor se a sitrng já estiver dividida
frase_dois = 'Curso', 'Em','Python'
print('-'.join(frase_dois)) # agoras sim... deu errado no outro exemplo porque a frase já estava junta
