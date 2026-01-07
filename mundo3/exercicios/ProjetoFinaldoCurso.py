#Nessa arquivo contem o ultimo exercício do curso, que contem as aulas 115 A, B e C
#Se trata de uma forma de criar um menu e cadastras informações dentro de um arquivo
from util.menu import itens
from util.arquivo import*
from time import sleep

arq = 'cursoemvideo.txt'

if arquivoExiste(arq):
    print('Arquivo encontrado com sucesso!')
else:
    print('Arquivo não encontradao')
    criarArquivo(arq)
    
while True:
    resposta = itens.menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        #opção de listar os conteúdos de um determinado arquivo
        lerArquivo(arq)
    elif resposta == 2:
        itens.cabeçalho('Novo cadastro')
        nome = str(input('Nome: '))
        idade = itens.leiaint('Idade: ')
        cadastrar(arq,nome,idade)
    elif resposta == 3:
        itens.cabeçalho('Saindo do sistema... até logo')
        break
    else:
        print('\033[31mErro! digite uma opção válida\033[m')
        sleep(2)