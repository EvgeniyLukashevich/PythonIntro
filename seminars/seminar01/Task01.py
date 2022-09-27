# Напишите программу, которая принимает на вход два числа 
# и проверяет является ли одно число квадратом другого

num1 = int(input('Please, input 1st number: '))
num2 = int(input('Please, input 2nd number: ')) 

print()

if num1 == num2 * num2:
    print(f'Yeah! {num1} is the square of {num2}')

elif num2 == num1 * num1:
    print(f'Yeah! {num2} is the square of {num1}')

elif num1 == num2:
    print('Try again. Your numbers is equal.')
    print(f'{num1} = {num2}')

else:
    print(f'{num1} is not the square of {num2}')
    print(f'{num2} is not the square of {num1}')
    print('Sorry, bro. Try again.')
