# Реализуйте алгоритм перемешивания списка

from random import randint

# Создание интового списка с запросом размера списка, мин и макс значений и случайной генерацией элементов (в диапазоне от мин до макс включительно) 
def CreateRandomIntList():

    size = int(input("Please, input the size of your list: "))
    minValue = int(input("Please, input the MIN possible value of an element: "))
    maxValue = int(input("Please, input the MAX possible value of an element: "))
    list = []

    for i in range(size):
        list.append(randint(minValue, maxValue))

    return list

# Миксер. Список может быть не только интовый.
def ListShuffle(list):

    newList = []

    for _ in range(len(list)):
        i = randint(0, len(list))
        newList.append(list[i])
        list.pop(i)

    return newList



list = CreateRandomIntList()
print(list)

mixedList = ListShuffle(list)
print(mixedList)
