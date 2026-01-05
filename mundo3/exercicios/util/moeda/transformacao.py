#Metade o dobro e +10% no total

#minha ideia inicial era jogar tudo dentro de uma função apenas, mas a proposta de resolução do professor
#foi separar cda função para facilitar a manutenção e legibilidade do código :D
def moeda(num):
    print(f'O dobro é {num * 2:.2f}')
    print(f'A metade é {num / 2:.2f}')
    #(num*10) / 100
    print(f'A soma de 10% a mais é {num + ((num * 10)/100)}')

#Resolução do professor
def aumentar(preco, taxa, formatacao= False):
    resposta =  preco + (preco * taxa / 100)
    if formatacao == True:
        return formata_moeda(resposta)
    else:
     return resposta
def diminuir(preco, taxa, formatacao= False):
    resposta = preco - (preco * taxa / 100)
    if formatacao == True:
        return formata_moeda(resposta)
    else:
     return resposta
def dobro(preco, formatacao= False):
    resposta = preco * 2
    if formatacao == True:
        return formata_moeda(resposta)
    else:
     return resposta
def metade(preco, formatacao= False):
    resposta = preco / 2
    if formatacao == True:
        return formata_moeda(resposta)
    else:
     return resposta

##108
#Resolução do professor
def formata_moeda(dinheiro = 0, moeda = 'R$'):
    return f'{moeda}{dinheiro:.2f}'.replace('.', ',') #isso aki é explicado na aula sobre manipulação de texto no mundo 1, muito útil
    
##109 foi colocar o 'formatacao' dentro de cada função acima

##110
def resumo(entrada = 0, taxa_aumento = 10, taxa_reducao = 5):
    print('-='*5,'','-='*5)
    print('Resumo do valor'.center(30))
    print('-='*5,'','-='*5)
    print(f'preço: {formata_moeda(entrada)}')
    print(f'Dobro: {formata_moeda(dobro(entrada))}')
    print(f'Metade: {formata_moeda(metade(entrada))}')
    print(f'Aumentar: {formata_moeda(aumentar(entrada, taxa_aumento))}')
    print(f'Diminuir: {formata_moeda(diminuir(entrada, taxa_aumento))}')
    print('-='*5,'','-='*5)
    return 'Fim'