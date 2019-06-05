
numbers = [] #zeros to place in the beginning
for i in range(int(input('numbers = '))):
    numbers.append(int(input('{}number = '.format(i+1))))
numbers1 = ([k for k in numbers if k==0])+([k for k in numbers if k!=0])
print(numbers)
print(numbers1)

