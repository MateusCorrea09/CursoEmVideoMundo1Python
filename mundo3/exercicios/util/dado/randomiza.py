#from random import randint
#from util.moeda import transformacao

def leia_dinheiro(msg):
    válido = False
    while not válido:
        valor = str(input(msg)).replace(',', '.')
        if valor.isalpha() or valor.strip() == '':
            print(f'Erro {valor} Preço inválido!')
        
        else:
            válido = True
            return float(valor)

            

    

