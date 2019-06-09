import random

number1 = random.randint(1, 10)
number2 = None

while number1 != number2:
    number2 = int(input('Number = '))
    continue
else:
    print('Stop')
