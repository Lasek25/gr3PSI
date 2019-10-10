print('{:>20}'.format('prawa'))
print('{:_<20}'.format('lewa'))
print('{:^20}'.format('srodek'))
print('{:.{prec}} = {:.{prec}f}'.format('wartosc',3.12461, prec=4))
tab = [11,31,22,-16,5]
print('{t[1]} {t[3]} {t[4]}'.format(t=tab))