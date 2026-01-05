# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e
#  vai retornar um dicionário com as seguintes informações:
#– Quantidade de notas     – A maior nota    – A menor nota   – A média da turma – A situação (opcional)
#eu acho que me perdi durante a execução desse exer´cicio e acabei fazendo outra coisa ?????
#quero dizer, esse exercício é mais simples do que eu fiz aki, só não vi a resolução e peguei apenas o enunciado :D
'''classe = list()
informacoes_turma = dict()
n_cadastros = 0
medida_nota_turma = 0
while True:
    aluno = dict()
    aluno['nome'] = str(input('Entre com seu nome: '))
    aluno['nota1'] = float(input('Entre com a primeira nota: '))
    aluno['nota2'] = float(input('Entre coma a segunda nota: '))
    
    aluno['media_final'] = (aluno['nota1'] + aluno['nota2']) / 2 
    if aluno['media_final'] > 6:
        aluno['situacao'] = 'aprovado'
    else:
        aluno['situacao'] = 'reprovado'
    classe.append(aluno.copy())

    n_cadastros += 1
    resposta = str(input('Deseja continuar? [s/n] '))
    if resposta == 'n':
        break
#achando as informações
soma_media_turma = 0
maior_nota = classe[0]['media_final']
menor_nota = classe[0]['media_final']
for i in classe:
    for key, value in i.items():
        if key == 'media_final':
            soma_media_turma += value
            if value > maior_nota:
                maior_nota = value
            if value < menor_nota:
                menor_nota = value

#salvamentos no dicionario:
informacoes_turma['n_cadastros'] = n_cadastros
medida_nota_turma = soma_media_turma / n_cadastros
informacoes_turma['media_turma'] = medida_nota_turma
informacoes_turma['maior_nota'] = maior_nota
informacoes_turma['menor_nota'] = menor_nota
#print(informacoes_turma)
while True:
    print('-='*5,'dados cadastrados','-='*5)
    cont = 0
    for i in classe:
        for key, value in i.items():
            print(f'{cont:<2}- {key:<.10} : {value:>.10}', end='||')
            cont += 1
        print()
    cont = 0
    print('-='*5,'informações sobre a turma','-='*5)
    for key, value in informacoes_turma.items():
        print(f'[{cont}]     - {key:<.10} : {value:<.2f}')
        cont += 1
    print()
    
    resp = str(input('Deseja saber a situação de algum aluno? [999 para sair!] '))
    valor = 0
    if resp == '999':
        break
    elif resp.isnumeric():
        valor = int(resp)
        print(informacoes_turma[valor])
    else:
        print('Entre com uma alternativa válida')
'''
#Exercício, feito junto com o professor
def notas(*n, sit = False):
    '''
    Docstring for notas:
    "Função apra analisar notar e situações de vários alunos"
    
    :param n: uma ou mais notas dos alunos
    :param sit: situação opcional para retornar a situação do aluno em relação as notas
    :return dicionário com várias informações sobre os alunos
    '''
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] > 7:
            r['situacao'] = 'Aprovado'
        elif r['media'] >= 5:
            r['situacao'] = 'Em recuperação'
        else:
            r['situacao'] = 'Reprovado'
    return r
resp = notas(1,2.5,8.5, sit=True)
print(resp)
resp = notas(1,2.5,8.5,10,9, sit=True)
print(resp)
resp = notas(1,2.5,8.5,4,9, sit=True)
print(resp)