#Crie u programa que leia o nome de uma pessoa e mostre:
#O nome com todas as letras maiúsculas
#O nome com todas minúsculas
#Quantas letras ao todo, sem espaçoz
#Quantas letras tel o primeiro nome 
nome = input('Entre com sue nome completo')
print('Seu nome com todas as letras Minúsculas é: [{}]'.format(nome.lower()))
print('Seu nome com todas as letras Maiúsuclas é: [{}]'.format(nome.upper()))
print('Seu nome tem um total de [{}] Letras'.format(len(nome.replace(' ','')))) #retirei o espaço e substitui ele por nada :D
primeiro_nome = nome.split()
print('O seu primeiro nome tem [{}] letras!'.format(len(primeiro_nome[0])))
