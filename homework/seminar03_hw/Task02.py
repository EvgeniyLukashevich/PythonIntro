# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

def CreateIntList():
    size = int(input('Please, input size of your list: '))
    list = []

    for i in range(size):
        list.append(int(input(f"Please, input {i+1} integer of {size}: ")))

    return list

# При нечетном количестве элементов, учитывает осевой элемент и умножает его на самого себя (как и указано в примерах к задаче)
def PairsProduct(list):
    newList = []

    for i in range(0, len(list) // 2):
        newList.append(list[i] * list[len(list) - 1 - i])

    if len(list) % 2 != 0:
        newList.append(list[len(list) // 2] **2)

    return newList

list = CreateIntList()
newList = PairsProduct(list)

print(f"Your list is {list}")

for i in range(0, len(newList)):
    print(f'Product of {list[i]} and {list[len(list) - 1 - i]} is {newList[i]}')
