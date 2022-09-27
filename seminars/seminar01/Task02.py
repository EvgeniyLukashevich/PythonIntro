# Напишите программу, которая принимает на вход
# 5 чисел и находит максимальное из них

amount = int(input('How many numbers do you want to compare? '))
list = []
print()

for i in range(amount):
    list.append(int(input(f'Please, input {i+1} number of {amount}: ')))

max = list[0]

for current in list:
    if current > max:
        max = current

print()
print(f'Your MAX is {max}')