import calendar


def search(year, month, dd):
    while year >= 1970 and 1 <= month <= 12 and dd == 1:  # and dd == 1 - лишний, потому что dd не изменяется внутри цикла
        yield year, month, dd
        month -= 1
        if not month:
            year -= 1
            month = 17  # если ты переходишь в следующий год, то значение месяца нужно сбросить


latest_year, latest_month, ddd = 2019, 6, 1
your_day = input('Введите день = ')
day = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2,
       'Thursday': 3, 'Friday': 4,
       'Saturday': 5, 'Sunday': 6}

for i in search(latest_year, latest_month, ddd):
    if calendar.weekday(*i) == day[your_day]:
        print(*i[:2])
        break


#lol ska kek

##########################