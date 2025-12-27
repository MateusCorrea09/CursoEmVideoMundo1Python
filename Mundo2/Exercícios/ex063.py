#0 – 1 – 1 – 2 – 3 – 5 – 8
#o resultado é a soma dos dois numeros anteriores, logo há um salvamento dos resultados
#do terceiro termo en diante Fn = F n-1 + F n-2 
entrada = int(input('Wuantos termos você quer mostrar? '))
cont = 3
resposta = 0
f1 = 0
f2 = 1
print('[{}] -> [{}]'.format(f1,f2), end='')
while cont <= entrada:
    resposta = f1 + f2
    print(' -> [{}]'.format(resposta), end='')
    f1 = f2
    f2 = resposta
    cont = cont + 1
print('fim')

    