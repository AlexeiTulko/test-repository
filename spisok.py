my_list = [10, 0,3,10,90,5]
number1 = 0
number2 = 0
for i in range(len(my_list)):
    if my_list[i] > number2:
        number2 = my_list[i]
    if my_list[i] > number1:
        k = number2
        number2 = number1
        number1 = k
print(number1, number2)
