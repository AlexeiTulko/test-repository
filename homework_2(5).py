def chain(a, b, c):
    return list(a) + list(b) + list(c)


for x in chain(range(3), range(1, 4), range(2, 5)):
    print(x)
