# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным 
# значением дробной части элементов

def CreateFloatList():
    size = int(input('Please, input size of your list: '))
    list = []

    for i in range(size):
        list.append(float(input(f"Please, input {i+1} real number of {size}: ")))

    return list

# Без перевода в строку. Логика работает, дробная порой часть чудит.
def MaxMinDiff(list):
    min = list[0] - int(list[0])
    max = list[0] - int(list[0])

    if max == 0.0:
        for i in range(1, len(list)):
            max = list[i] - int(list[i])
            min = list[i] - int(list[i])
            if max != 0.0: break

    for i in range(1, len(list)):
        if list[i] - int(list[i]) == 0.0: continue
        if list[i] - int(list[i]) > max:
            max = list[i] - int(list[i])
        if list[i] - int(list[i]) < min:
            min = list[i] - int(list[i])
    
    print(f'Max is {max}')
    print(f'Min is {min}')
    return max - min

list = CreateFloatList()
print(f"Your list is {list}")
result = MaxMinDiff(list)   
print(f"Result is {result}")