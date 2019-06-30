import calendar


Y = int(input('Year = '))
M = int(input('Month = '))
D = int(input('Day = '))

x = calendar.weekday(Y, M, D)
# можно было использовать calendar.day_name
if x == 0:
    print('Monday')
elif x == 1:
    print('Tuesday')
elif x == 2:
    print('Wednesday')
elif x == 3:
    print('Thursday')
elif x == 4:
    print('Friday')
elif x == 5:
    print('Saturday')
else:
    print('Sunday')
