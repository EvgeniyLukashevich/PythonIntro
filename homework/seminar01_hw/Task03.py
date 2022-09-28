# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится)
# 
# Не оч понял, зачем ограничивать пользователя на введение нуля, 
# если по условию есть возможность сообщить, что точка лежит на оси. 
# Наверное имеется в виду ограничение на введение нуля и нуля, 
# но и в этом случае можно сказать пользователю, типа: "бро, ты на нуле".
# Попробую так и сделать)

def WhatQuarter(x, y):
    if x > 0 and y > 0: 
        print('Your point is in the 1st quarter')
    
    elif x < 0 and y > 0:
        print('Your point is in the 2nd quarter')

    elif x < 0 and y < 0:
        print('Your point is in the 3rd quarter')

    elif x > 0 and y < 0:
        print('Your point is in the 4th quarter')
    
    elif x == 0 and y != 0:
        print('Your point is on the x-axis')

    elif x != 0 and y == 0:
        print('Your point is on the y-axis')

    else:
        print('Your point is at the origin, bro')

x = int(input('Please input a value for x: '))
y = int(input('Please input a value for y: '))

WhatQuarter(x, y)