#faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' e 'F'
#Caso esteja errado, peça para a digitação ocorrer novamente até ter um valor correto
controle  = 1 #criei uma variavel de controle para fazer esse algoritimo funcionar
while controle == 1:#não consegui fazer uma verificação dupla com 's' ou 'm'
    entrada = str(input('ENTRE COM SEU GENERO [S] ou [M]:  ')).lower()
    if entrada == 'm' or entrada == 's':
     controle = 0
    else:
        print('Entre com uma das opções acima')
print('A entrada foi contabilzada!')

#resolução do professor
#o professor escolheu colocar a entrada fora do loop
sexo = str(input('Entre com seu genero [f / m]: '))
while sexo not in 'MmFf': #tinha esquecido dessa escrita!
                            #é dessa forma que crio as erificações dentro da estrutura while
#Nessa parte do 'Not in' e logo em seguida ele criou uma variavel local sem nome e atribui um conteúdeo 'MmFf' para fazer essa verificação... com todas as possibilidades dentro desse range de opções
   print('entre com uma das opções')
   sexo = str(input('Entre com seu genero [m / f] : '))
print('Fim da aplicação!')