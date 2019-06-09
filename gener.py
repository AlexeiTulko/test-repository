def count(a, b=1):
    while True:
        yield a
        a += b


for i in count(int(input('Введите число = ')), 2):
    print(i)
    if i >= 100:
        break
