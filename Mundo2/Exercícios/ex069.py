#Crie um programa que leia a idade e o sexo de várias pessoas. A cada
# pessoa cadastrada, o programa deverá perguntar se quer ou não continuar.
# no final, mostre:
# quantas pessoas tem mais de 18 anos
# quantos homens foram cadastrados
# quantas mulheres tem menos de 20 anos

maior_idade = quant_homens = quant_mulher = 0
while True:
    s = str(input('Entre com seu genero [F / M]: ')).upper()
    idade = int(input('Entre com sua idade: '))
    if idade > 18:
        maior_idade += 1
        if s == 'F':
            quant_mulher += 1
    if s == 'M':
        quant_homens += 1
    resposta = str(input('Deseja continuar [S / N ]?: ')).upper()
    if resposta == 'N':
        break
print('Quantidade de pessoas com idade maior ou igual a 18 anos [{}]'.format(maior_idade))
print('Quantidade de homens cadastrados [{}]'.format(quant_homens))
print('Quantidade de mulheres cadastradas [{}]'.format(quant_mulher))