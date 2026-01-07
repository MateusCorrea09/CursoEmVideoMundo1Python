def titulo(msg):
    print(f'{"-"*8} {msg} {"-"*8}')
    #print(f'{msg:<.10}')

def botao(numero, nome):
    tamanho = len(nome) + 4
    print('_' * tamanho)
    print(f'[{numero}] -   {nome}')
    print('_' * tamanho)

def acesso_alternativa(num,lista_alternativas):
    try:
        nome_botao = lista_alternativas[num]
        tamanho = len(lista_alternativas[num])
        print(f'-' * tamanho)
        print(f'{nome_botao}')
        print(f'-' * tamanho)
    except Exception as erro:
        print(f'ERRO! {erro.__class__}')

def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('Erro por favor digite um número inteiro válido')
            continue
        except KeyboardInterrupt:
            print('O usuário preferiu não digitar esse número')
            return 0
        else:
            return n

def menu(n_botoes):
    '''
    Docstring for menu
    
    :param titulo: Entrada referente ao titulo do  menu
    :param n_botoes: inteiro referente ao número de botões que terão no menu
    '''
    cont_botoes = 1
    nome_botoes = list()
    while cont_botoes <= n_botoes:
        try:
            nome_botoes.append(str(input(f' Entre com o nome do botão Nº [{cont_botoes}]: ')))
            cont_botoes += 1
        except KeyboardInterrupt:
            print('o usuário interroupeu a ação')
            continue
    nome_botoes.append('SAIR!')
    titulo_menu = str(input('Entre com um titulo para seu menu: '))
    titulo(titulo_menu)
    for numero,i in enumerate(nome_botoes):
        botao(numero, i)
    while True:
        try:
            entrada = int(input('Entre com uma das opções acima: '))
        except Exception as erro:
            print(f'ERRO [{erro.__class__}] [{erro.__cause__}]')
        finally:
            try:
                #print(len(nome_botoes))
                if entrada == len(nome_botoes) - 1:
                    print('Até a proxima!')
                    break
                acesso_alternativa(entrada,nome_botoes)
            except Exception as erro:
                print(f'ERRO {erro.__class__} {erro.__cause__}')
    
#Aqui é referente ao projeto 
def linha(tam = 42):
    return '- ' * tam

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabeçalho('Menu principal')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaint('\033[32mSua opção: \033[m')
    return opc