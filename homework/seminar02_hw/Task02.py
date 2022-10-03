# Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.

def MultiplyOneToN(num):
    
    multiply = 1
    result = []

    if num >= 1:
        for i in range(1, num + 1):
            multiply *= i 
            result.append(multiply)
    
    else:                                       # Если введенное число отрицательное, то двигаясь от единицы к нему, будем проходить через 0. 
        for i in range(1, num - 1, -1):         # И, соответственно, все последующие числа в списке после единицы будут умножаться на ноль
            multiply *= i                       # Можно было бы обходить ноль, но тогда это получится не очень по условию задачи
            result.append(multiply)

    return result

num = int(input('Please input an integer: '))

print(f'N is {num}. Result is {MultiplyOneToN(num)}')