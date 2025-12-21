#faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente
#desse ângulo.
import math
agulo = float(input('Entre com um angulo: '))
seno = math.sin(math.radians(agulo)) # já pega o 'sin' pasando como argumento outro método que vai gerar um resultado
                                    #é tipo um método que retorna um resultado mas antes de retornar ele espera o resultado de outro método dentro dele :D
print('o SENO de [{:.3f}] é [{:.3f}]'.format(agulo,seno))
cosseno = math.cos(math.radians(agulo))
print('O COSSENO de [{:.3f}] é [{:.3f}]'.format(agulo,cosseno))
tangente = math.tan(math.radians(agulo))
print('A Tangente de [{:.3f}] é [{:.3f}]'.format(agulo,tangente))