#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
#  No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar 
#  as notas de cada aluno individualmente.

dados = list()
dados_entrada_Lista = list()
lista_alunos = list()
lista_notas_finais = list()
while True:
    soma_media = 0
    dados.append(str(input('Entre com o nome: ')))
    dados.append(float(input('Entre com a primeira nota do aluno: ')))
    dados.append(float(input('Entre com a segunda nota do aluno: ')))
    dados_entrada_Lista.append(dados[0])
    
    #lista_notas_finais.append(dados_entrada_Lista[0][0])
    #print(dados_entrada_Lista)
    soma_media = (dados[1] + dados[2]) / 2
    dados_entrada_Lista.append(dados[1])
    dados_entrada_Lista.append(dados[2])
    dados.clear()
    #print(soma_media)
    dados_entrada_Lista.append(soma_media)
    lista_notas_finais.append(dados_entrada_Lista[:])
    #print(lista_notas_finais)
    dados_entrada_Lista.clear()
    resposta = str(input('Deseja continuar?[s/n] ')).lower()
    if resposta =='n':
        print('--Obrigado e volte sempre--')
        break
print('[*]'*30)
print(lista_notas_finais)
print('[*]'*30)

#Nesse ponto as notas estão sendo registradas, eu preciso criar uma matrix auxiliar
# para receber o nome do aluno e em seguida a media dele. e depois eu exibi essa matrix e 
# uso o indice dela para indicar as notas que foram salvas, caso o usuário deseje saber
# quais notas determinado aluno tirou
#Eu preciso agora criar um loop pra mostrar as notas uma a baixo da outra por meio dos índices




"""for i in range(0,3):
    
    soma_media = 0
    for j in range(0,3):
        #declarando variavel local para atribuir a media
        
        #pegando o nome do aluno
        if j == 0:
         dados.append(lista_alunos[i][j])
        #pegando a média do aluno
        if j == 2:
            soma_media = (lista_alunos[i][j] + lista_alunos[i][j - 1]) / 2
            dados.append(soma_media)
            lista_notas_finais.append(dados[:])
            dados.clear()
for i in range(0,3):
    for j in range(0,2):
        print(lista_notas_finais[i][j])
    print()"""