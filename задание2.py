print ('Вариант 1')
first = input ('Введите первое число ')
second = input ('Введите второе число ')
third = input ('Введите третье число ')
a = {first, second, third}
b = len (a)
if b == 1:
    print (3)
elif b == 2:
    print (2)
else:
    print (0)
print ('Вариант 2')
first = input ('Введите первое число ')
second = input ('Введите второе число ')
third = input ('Введите третье число ')
if first == third == second:
    print (3)
else:
    if first == third or third == second:
        print (2)
    elif first == second:
        print (2)
    else:
        print (0)

