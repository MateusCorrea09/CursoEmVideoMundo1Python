#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os
# em uma tupla. No final, no final mostre:
# quantas vezes apareceu o valor 9
# em qua posição foi digitado o primeiro valor 3
# quais foram os números pares
#a = int(input('Entre com o primeiro número: '))
#b = int(input('Entre com o segundo número: '))
#c = int(input('Entre com o penúltimo número: '))
#d = int(input('Entre com o últumo número: '))
#tupla=(a,b,c,d)

#Eu fiquei meio encomodado com essa solução... parece um for... só que diferente 
tupla = (int(input('Entre com um n: ')),
         int(input('Entre com um n: ')),
         int(input('Entre com um n: ')),
         int(input('Entre com um n: ')),
         int(input('Entre com um n: ')))
print(f'O número 9 apareceu um total de = [{tupla.count(9)}] vezes')
print(f'O primeiro valor 3 aparece na posição [{tupla.index(3) + 1}]')
cont = 0
for i in tupla:
    if i % 2 == 0:
        cont = cont + 1
print(f'A um total de [{cont}] números pares')