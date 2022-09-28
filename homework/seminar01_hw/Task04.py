# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

# Захотелось немного "помучить" пользователя пока он корректно не введёт номер четверти.
# Тип переменной оставил строковым, чтобы программа реагировала на большее количество вариантов неверного ввода
# В общем, не уверен, что попытка удачная, но что касается задачи, она, вроде, решена :) 


num = input('Please input number of quarter: ')

while num != '1' and num != "2" and num != '3' and num != '4':
    print("Don't upset me, dude. You need to input '1', '2', '3' or '4'")
    print("Number of Quarter, you know? Let's try again.")
    num = input('Please input number of quarter: ')

if num == '1':
    print('x(0; +inf); y(0; +inf)')

elif num == '2':
    print('x(0; -inf); y(0; +inf)')

elif num == '3':
    print('x(0; -inf); y(0; -inf)')

else:
    print('x(0; +inf); y(0; -inf)')