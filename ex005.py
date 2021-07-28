medida = float(input('Uma distancia em metros:'))
cm = medida * 100
mm = medida * 1000
dm = medida * 10
dac = medida / 10
hec = medida / 100
km = medida / 1000
print('a medida de {}m,\ncorresponde a {:.0f}cm, {:.0f}mm, {:.0f}dm, {}dac, {}hec e {}km'.format(medida,cm, mm, dm, dac, hec, km))