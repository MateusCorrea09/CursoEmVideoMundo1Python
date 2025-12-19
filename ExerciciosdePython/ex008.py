#Crie um algoritimo que receba uma entrada e realiza uma série de conversões
medida = float(input('entre com os metros'))
cm = medida * 100
mm = medida * 1000

print('a medidad de {}m corresponde a {:.0f}cm e{:.0f}mm'.format(medida,cm,mm))

dam = medida / 10
hm = medida / 100
km = medida / 1000
print('a medida de {}m corresponde a {}dam, {}hm e {}km'.format(medida,dam,hm,km))