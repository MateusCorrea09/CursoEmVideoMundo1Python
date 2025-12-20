#pelo que eu entendi esses módulos são adicções que fazemos no python
#para utilizar dês de ferramentas que já vem instaladas ou ferramentas de fora
#para essa aula focaremos em utilizar o math, e suas ferramentas que vem nesse módulo

import math
import random
import emoji #instalei um módulo sugerido pelo vídeo

print(emoji.emojize("Python é top :thumbs_up:")) #aplicando o módulo em um pint
num = int(input('entre com um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a  {}'.format(num, math.ceil(raiz))) #usando o sqrt 
#math.ceil permite arredondar o valor
num_random = random.random()
print(num_random) # gera um número float entre 0 e 1
num_random_int = random.randint(1,10) #gera um número inteiro de 1 a 10
print(num_random_int)
