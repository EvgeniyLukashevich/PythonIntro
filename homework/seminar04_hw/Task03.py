# TASK 3. Задайте последовательность цифр. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности

from random import randint 

def CreateIntList():
    size = int(input('Please, input size of numbers sequence: '))
    list = [randint(1, 9) for i in range(size)]
    return list
         
def UniqueIntList(list1):
    sequence =''.join(list(map(str, list1)))
    dict = {}
    result = []

    for c in sequence:
        if dict.get(c):
            dict[c] += 1
        else: dict[c] = 1
    
    for i in dict.items():
        if i[1] == 1:
            result.append(int(i[0]))

    return result

    
originList = CreateIntList()
resultList = UniqueIntList(originList)
print(f"Origin list is: {originList}")
print(f"Result list is: {resultList}")