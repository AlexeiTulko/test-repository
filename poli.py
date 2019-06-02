word = str(input('insert your word = '))
ind = word[::-1] #переменная полная копия слова, но читается с конца
if word == ind: # если слово, читаемое с конца, идентично оригиналу, то это полиндром
    print('that\'s cool, mate')
else:
    print('nuh, this shit is not a palindrome')
print(word)
