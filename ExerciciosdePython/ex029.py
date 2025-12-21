#Escreva um programa que loeia a velocidade de um carro. Se ele ultrapassa 80km/h,
#mostre uma mensagem dizendo que ele foi multado.
#   A multa vai custar R$7,00 por cada km acima do limite
velocidade = float(input('👮🚓🚨 Entre com a velocidade do automóvel: 👮🚓🚨\n'))
if velocidade <= 80:
    print('🤙Você está dentro do limite! se mantenha assim para evitar acidentes🤙')
else:
    multa = (velocidade - 80) * 7
    print('💢Você está acima da velocidade!💢\n 💸E sofrerá uma multa no valor de [R${:.2f}]💸'.format(multa))