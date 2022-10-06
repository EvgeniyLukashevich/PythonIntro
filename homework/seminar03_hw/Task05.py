# Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов

def FiboNegafibo(size):
    list = [-1 ,1, 0, 1, 1]

    if size > 1:
        for i in range(5, size + 3):
            list.append(list[i - 1] + list[i - 2])
        for i in range(2, size):    
            list.insert(0, list[1] - list[0])
    
    elif size == 1: return [1, 0, 1]
    
    else: return "Count of Fibonacci numbers is uncorrected"

    return list;  

print(FiboNegafibo(2))
