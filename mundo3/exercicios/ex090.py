# faça um programa que leia nome e média de um aluno, guardando
# também a situação em um dicionário. No final, mostre o conteúdo
# da estrutura na tela

aluno = dict() #ele tem nome, media e situação que usa if
aluno['nome'] = str(input('Entre com seu nome: '))
aluno['media'] = float(input(f'Entre com a média de [{aluno["nome"]}]: '))
if aluno['media'] > 6:
    aluno['situacao'] = 'Aprovado'
else:
    aluno['situacao'] = 'Reprovado'
for key, value in aluno.items():
    print(f' {key} : {value}', end= " -> ")