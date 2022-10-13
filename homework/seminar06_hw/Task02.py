# # Задайте список из нескольких чисел. Напишите программу, 
# # которая найдёт сумму элементов списка, стоящих на нечётной позиции

# from random import randint


# def CreateIntList():
#     size = int(input('Please, input size of your list: '))
#     list = []

#     for i in range(size):
#         list.append(int(input(f"Please, input {i+1} integer of {size}: ")))

#     return list

# def SumOfOddPositionElements(list):
#     result = 0

#     for i in range(0, len(list), 2):
#         result += list[i]

#     return result

# list = CreateIntList()
# sum = SumOfOddPositionElements(list)

# print(f"Your list is {list}")
# print(f"Sum of integers on odd positions is {sum}")


# За нечетные позиции принял первую, третью, пятую и тд. То есть индексы 0, 2, 4 и тд.
from random import randint

list1 = [randint(1,10) for _ in range(int(input('Please input size of origin list: ')))]        # list comprehension
result = [list1[i] for i in list(filter(lambda x: x % 2 == 0, range(len(list1))))]              # lambda, filter, list comprehension
sum1 = 0

for x in result:
    sum1 += x
    
print(f'The origin list is {list1}')
print(f'The result list is {result}')
print(f'The result is {sum1}')