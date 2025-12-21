#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes a letra 'A' aparece
#Em que posição ele aparce primeiro
#Em que posição ele aparece a ultima vez
frase = input('Entre com uma frase: ').lower()
print('A letra [A] aparacere um total de: [{}]'.format(frase.count('a')))
print('A letra [A] aparece primerio na posição [{}]'.format(frase.find('a') + 1))
print('A ultima posição da letra [A] é [{}]'.format(frase.rfind('a')))# deve usar o 'r' em 'find' ... junto formam o 'rfind()' que seri um 
                                                                    #"Começe a procurar a letra [a] a aprtir da ultima posição da frase"
                                                                    #ou 'comece a contrar a aprtir do lado 'direito' da lista