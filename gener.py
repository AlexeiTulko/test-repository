def count(a, b=1):
    while True:
        yield a
        a += b


for i in count(int(input('Введите число = ')), 2):
    # старайся не писать такие сложные выражения, как count(int(input('Введите число = ')), 2)
    # лучше разбить их на несколько инструкций, например:
    # n = int(input())
    # for i in count(n, 2): ...
    print(i)
    if i >= 100:
        break
