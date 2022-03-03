d = float(input('enter distance:   '))
tar = float(input('enter target distance:  '))
day = 1
while d < tar:
    d *= 1.1
    day += 1
print(f' summa days: { day}')