# TASK 2. Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N

# Насколько я помню, простые множители - те, которые делят без остатка :)

def Factorization(num):
    list = [ ]
    d = 2
    temp = num

    while temp > 1:
        if temp % d == 0:
            list.append(d)
            temp /= d
        else: d += 1   
        
    if len(list) == 1:
        list.insert(0, 1)
        print(f'{num} is a prime number')

    return list

n = int(input('Please, input your integer: '))
list = Factorization(n)

print(f'Catch the factorization of {n}:\n{list}')
