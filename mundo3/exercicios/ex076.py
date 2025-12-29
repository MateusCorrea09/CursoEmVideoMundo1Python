#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
#  na sequência. No final, mostre uma listagem de preços, organizando os dados em forma
#  tabular.
tupla = ('x-burguer',5.70,'X-Salada',3.50,'Batata-Frita',9.50,'Coca-Cola', 3.80,'Fanta', 2.45)
for posicao in range(0,len(tupla)):
    #Dessa forma apenas apresenta os índices pares, que sabemos que tem os nomes dos produtos
    if posicao % 2 == 0:
        #Esse é um conhecimento especifico de python e tem haver com a utlização da limitação de 
        #caracteres a serem printados na tela 'tupla[posição]:30' diz que só serão printados no máximo 30
        #caracteres ... então se tiver um item com mais de 30 caracteres ele será cortado, mas como sabemos
        #que na tupla não há nenhum item com esse número de caracteres isso não ocorre
        # agora com a adicção do '.' no meio da seguinte forma 'tupla[posição]:.30' o ponto preenche o espaço vazio
        # até chegar no ultimo caractere possível a ser printado na tela que seria o da posição '30'
        #logo formando uma solução agradável :D na aula de manipulação de string ele explica isso melhor
        print(f'{tupla[posicao]:.<30}',end='')
    else:
        #é realmente uma coisa ligada a prática e tornar soluções assim
        #parte a sua escrita com línguagem (decoreba)
        print(f'R${tupla[posicao]:>7.2f}')