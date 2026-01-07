from util.menu import itens
def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print('Arquivo criado com sucesso!')
def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        itens.cabeçalho('Pessoas cadastradas')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:3} anos')
    finally:
        a.close()
def cadastrar(arq, nome = 'descohecido', idade = 0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um problema na abertuda do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('houve um problema na escrita da nova entrada')
        else:
            print(f'Novo registro {nome} adicionado com sucesso!')

