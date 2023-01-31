medida = float(input('uma distancia em metros: '))
km = medida / 10000
hm = medida / 1000
dam = medida / 100
dm = medida * 10
cm = medida * 100
mm = medida * 1000

print('a medida de {}m corresponde a {} dm\n {} cm\n {} mm\n {} dam\n {} hm\n {} km\n'.format(medida, dm, cm, mm, dam, hm, km))
