# Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
#  calcule seu Índice de Massa Corporal (IMC) e mostre seu status,
#  de acordo com a tabela abaixo:
#IMC abaixo de 18,5: Abaixo do Peso
#Entre 18,5 e 25: Peso Ideal
#25 até 30: Sobrepeso
#30 até 40: Obesidade
#Acima de 40: Obesidade Mórbida
entrada_peso = float(input('Entre com seu peso: '))
entrada_altura = float(input('Entre com sua altura: '))
resultado_imc = entrada_peso / pow(entrada_altura,2)
if resultado_imc < 18.5:
    print('Abaixo do peso')
elif 18.5 < resultado_imc <= 25:
    print('Peso ideal')
elif 25 < resultado_imc <= 30:
    print('Sobrepeso')
elif 30 < resultado_imc <= 40:
    print('Obesidade')
elif resultado_imc > 40:
    print('Obesidade Mórbida')