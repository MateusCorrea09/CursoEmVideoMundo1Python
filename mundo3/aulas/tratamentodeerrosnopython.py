#Erros, exeções e tratamentos de erro :D
#'Erros acontecem' e vc tem que estar preparado para tratar essas respectivas falhas
#existem algumas formas de tratar esses erros, então busque nas língaugens que vc usa como
#como ela disponibiliza essas respectivas ferramentas de tratamento

#Exemplo
#'primt(x)' -> é um erro de "sintaxe" pois o erro é uma falha na escrita
#agora em, 'print(x)' não hpa erros de sintaxe... 'Estar certo e livre de erros é bem diferente'
#No caso acima o erro do 'print(x)' é que 'x' não foi declarada ainda, logo resultará em um erro
#assim não é um erro de sintaxe e sim semântico, assim resiltando em um 'NameErro'
#quando isso acontece não damos o nome de 'ERRO' e sim de execão

#Em um n = int(input('Num')) está correto... mas um usuário pode digitar algo que não seja um inteiro ou uma string 
#como 'Oito' que resultaria em um erro, pois 'n' espera um inteiro. Resultando um 'ValueError'

#Em uma divisão como 'r = a / b' pode estar correta visualmente... mas se o 'b' for uma entrada = 0 dará um erro
#  de divisão por zero 'ZeroDivisionError'
#Nesse mesmo último exemplo se 'r = a / b' e algumas das entradas 'a' ou 'b' for por exemplo '2' (isso significa ser uma string)
#resulta em um 'typeError' um erro de tipo

#Existem diversas formas de exeções e decorar elas não é o caminho, e sim entender oq pode ser feito e como trata-las... fique calmo :D

#_______________________________________________________
#para tratar uma exeção usamos o 'try:' 'except:'
#exemplo:
try: # Tente fazer
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError): # exiba se der erro / Use o 'Exception' para exibir para o usuário o determinado erro
    print(f'Tivemos um problema com os tipos de dados que vc digitou')
except ZeroDivisionError:
    print('Erro de divisão por zero')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
except Exception as erro:
#Essa parte '[nome da variavel que armazena o erro].__class__' exibe o determinado erro para que o usuário saiba do que se trata
    print(f'O erro encontrado foi {erro.__cause__} \n {erro.__class__}')
else: # se der tudo certo
    print(f'O resultado é {r}')
finally: # faça se der certo ou se der errado
    print('Volte sempre!')

#Essa ferramenta de tratamento de erros pode ser utilizada em uma enorme ramificação
#com um tratamento específico para cada tipo de erro com o 'except [erro]:'

