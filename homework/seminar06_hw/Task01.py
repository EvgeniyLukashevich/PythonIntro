# Задайте список из n чисел последовательности 
# (1+1/n)^n и выведите на экран их сумму

# def Posl2(num):                             
    
#     result = []

#     for i in range(1, num + 1):
#         result.append(round((1 + 1 / i)**i, 3))

#     return result


# num = int(input('Please input an integer > 0 : '))

# if num < 1:
#     print("Sorry, bro. Your number must be greater than 0")
# else:
#     print(Posl2(num))



num = int(input('Please input an integer > 0 : '))

if num < 1:
    print("Sorry, bro. Your number must be greater than 0")
    exit()
else:
    result = list(map(lambda num: round((1+1/num)**num, 3), [num for num in range(1, num+1)]))      # lambda, map

print(result)