# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции

def CreateIntList():
    size = int(input('Please, input size of your list: '))
    list = []

    for i in range(size):
        list.append(int(input(f"Please, input {i+1} integer of {size}: ")))

    return list

def SumOfOddPositionElements(list):
    result = 0

    for i in range(0, len(list), 2):
        result += list[i]

    return result

list = CreateIntList()
sum = SumOfOddPositionElements(list)

print(f"Your list is {list}")
print(f"Sum of integers on odd positions is {sum}")

