# Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.

num = int(input('Please, input number of your day of the week: '))

if num == 6 or num == 7:
    print('Yeah! Your day is a day off!')

elif num > 0 and num < 6:
    print('Sorry, your day is a working day')

else:
    print('Oops... There are seven days in a week')
    print('You need to enter a number from 1 to 7, bro.')