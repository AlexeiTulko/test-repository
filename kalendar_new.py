import calendar

day = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday',
       3: 'Thursday', 4: 'Friday',
       5: 'Saturday', 6: 'Sunday'}

print(day[calendar.weekday(int(input('Год = ')), int(input('Month = ')), int(input('Day = ')))])
