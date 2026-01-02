#Faça um programa que tenha uma função chamada escreva(), que receba um 
# texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável. 


def escreva(texto):
    tamanho_texto = len(texto) + 4
    print("~"*tamanho_texto)
    print(f' {texto} ')
    print("~"*tamanho_texto)

escreva('ALOOOOOOO')
escreva('Mateus Corrêa')
escreva('Olá mundo!')