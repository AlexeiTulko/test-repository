
numbers = [] #zeros to place in the beginning
for i in range(int(input('numbers = '))):
    numbers.append(int(input('{}number = '.format(i+1))))
numbers1 = sorted(numbers) #не понимаю, как перенести нули, не отсортировав список
print(numbers)
print(numbers1)
