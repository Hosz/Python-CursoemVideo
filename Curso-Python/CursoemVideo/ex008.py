n = float(input('Digite uma medida em metros: '))
km = n/1000
hm = n/100
dam = n/10
dm = n*10
cm = n * 100
mm = n * 1000
print('A área em km é {}km. \nA área em hm é {}hm. \nA área em dam é {}dam. \nA área em dm é {:.0f}dm. \nA área em cm é {:.0f}cm. \nA área em mm é {:.0f}mm.'.format(km, hm, dam, dm, cm, mm))