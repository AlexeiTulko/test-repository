
my_list = [78, 7000, 39, 60000, 88]  # предыдущее решение было читерским, сделал через цикл
number = 0
for r in my_list:
    if r > number:
        number = r
print(number)
