# Напишите программу, которая будет преобразовывать
# десятичное число в двоичное

def BinaryNumber(num):
    result = ""

    while num > 0:
        result = f"{num % 2}{result}"
        num //= 2

    return int(result)

num = int(input('Please, input an integer: '))
result = BinaryNumber(num)

print(f'The result is {result}')