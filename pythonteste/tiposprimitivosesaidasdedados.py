#podemos mostrar o tipo de uma variavel utilziando um comando chamado 'type()'
#isso pode paracer sem graça ou não utilziavel, mas é importante saber que podemos
#identificar qual determinado tipo de variavel esta sendo trabalhada, inclusive
#pode apareer em uma prova algo similar.
n1 = 12 #nessa parte eu sei que é um inteiro, mas eu posso fazer um print
        #me mostrar o tipo de 'n1'
print(type(n1)) #resultado esperado : 'int'
#se por algum acaso você se esquecer de fazer a conversão para int, em um input será
#considerado um 'str', exemplo
n2 = input('Entre com um número: ')#perceba que eu não fiz a conversão com 'int(input('entre com um número'))'
print(type(n2))# resultado esperado 'str' (QUE SERIA UMA STRING)

#exercicios proposto durante a aula#
#faça no print exibir as entradas do usuário e exibir o resultado da soma entre elas
n3 = int(input('Entre com um número: '))
n4 = int(input('Entre com um númeor'))
resp = n3 + n4
print('a soma de [{}] e [{}] é [{}]'.format(n3,n4,resp))
##fim do exercício

#é possível fazer uma verificação de se determinada entrada pertence a um grupo de dados
#no sentido de identificar se uma entrada é 'numérica' ou 'alfabética' sempre retornando um True ou False
n = input('Entre com algo:')
print('é um alfabeto? ',n.isalpha()) #para perguntar se é um alfabeto
print('é um numérico? ',n.isnumeric()) #para ssaber ser é numérico
print('está tudo em minusculo? ',n.islower()) #para saber se tudo está minusculos
print('está tudo em maiúsculo? ',n.isupper()) #para saber se ta tudo em maiúsculo