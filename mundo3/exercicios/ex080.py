#Crie um programa onde o usuário possa digitar cinco valores numéricos e 
# cadastre-os em uma lista, já na posição coreta da inserção sem usar o
# sort()
# no final, mostre a lista ordenada na tela.

lista_numerica = []
for c in range(0,5):
    entrada = int(input('Entre com um número: '))
    if c == 0 or entrada > lista_numerica[-1]: #isso aki impede que a lista quebre, ela adiciona +1 elemento de for o primeiro e se a entrada for maior que o ultimo item da lista... ai ele da o 'append()'
        lista_numerica.append(entrada)
    else: #do contrario ele vai tentar pegar a entrada e comparar com os elementos dentro da lista
        pos = 0 #uma variavel de controle para andar pelas posições da lista
        while pos < len(lista_numerica): #vai comparar se o número de posições andadas ainda está dentro do range da lista
            if entrada <= lista_numerica[pos]: #checa se o conteúdo da posição é o mesmo da entrada
                lista_numerica.insert(pos,entrada) # se for igual ou menos ele da um insert na mesmo posição, forçando o item a se deslocar uma posição apra frente
                break
            pos +=1
print(lista_numerica)

        #Eu tenho aque ir na posição e dar append para adicionar depois  