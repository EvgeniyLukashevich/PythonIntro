# Задайте список из n чисел последовательности 
# (1+1/n)^n и выведите на экран их сумму

def Posl1(num):                             # Без округления
    
    result = []

    for i in range(1, num + 1):
        result.append((1 + 1 / i)**i)

    return result

def Posl2(num):                             # С округлением до трёх знаков после запятой
    
    result = []

    for i in range(1, num + 1):
        result.append(round((1 + 1 / i)**i, 3))

    return result

def Posl3(num):                             # С округлением до целых чисел
    
    result = []

    for i in range(1, num + 1):
        result.append(round((1 + 1 / i)**i))

    return result


num = int(input('Please input an integer > 0 : '))

if num < 1:
    print("Sorry, bro. Your number must be greater than 0")
else:
    print(Posl2(num))