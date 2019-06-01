hour = float(input('x = '))
if hour < 25 and hour % 2 == 0:
    print('even')
elif hour % 2 != 0 and hour < 25:
    print('uneven')
else:
    print('no more hours')
