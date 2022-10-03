# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число

from random import randint

def CreateListNSize(n):
    
    list = []

    for i in range(n):
        list.append(randint(-n, n))
    
    return list

    


num = int(input('Please input an integer: '))
list = CreateListNSize(num)

with open ('homework/seminar02_hw/file.txt') as f:
    pos1 = int(f.readline())
    pos2 = int(f.readline(1)) 
    
                                                                                            
print(list)
print(f'{list[pos1 - 1]} * {list[pos2 - 1]} = {list[pos1 - 1] * list[pos2 - 1]}')       # В индексе проставил pos - 1, т.к. индекс элемента на единицу меньше его позиции
