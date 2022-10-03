# Напишите программу, которая принимает на вход 
# вещественное число и показывает сумму его цифр

# Хотел решить без перевода в строку, но в пайтоне с дробями, конечно, приколюх хватает)))

def SumOfDigits1(num):              # Иногда дробная часть становится страшной. Из-за этого результат слетает... 
    
    result = 0

    while num - int(num) != 0:
        
        print(f'{num} - {int(num)} = {num - int(num)}')         # поставил принты, чтобы видеть что происходит
        num *= 10
    
    num = int(num)
    print(num)

    while num != 0:
        result += int(num % 10)
        num /= 10
    
    return result


def SumOfDigits2(num):              # С переводом в строку. Работает.
    result = 0

    for i in str(num):
        if i == '.' or i == '-': continue
        else:
            result += int(i)
    
    return result

                            
def SumOfDigits3(num):              # Число-ограничитель в первом цикле такое, т.к. близкое к нулю и позволяет многие (но не все) ошибки из-за дробной части избежать
                                    
    result = 0

    while num - int(num) > 0.00000000000009:
        print(f'{num} - {int(num)} = {num - int(num)}')
        num *= 10
    
    num = int(num)
    print(num)

    while num != 0:
        result += int(num % 10)
        num /= 10
    
    return result

n = float(input('Please input your number: '))

print(f"Sum of digits of {n} = {SumOfDigits2(n)}")