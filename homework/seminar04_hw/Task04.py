# TASK 4. Задана натуральная степень k. Сформировать случайным образом
# список коэффициентов (значения от -100 до 100) многочлена и записать в файл многочлен степени k.
# k - максимальная степень многочлена, степень следующего на 1 меньше и так до ноля.
# Коэффициенты расставляет random, поэтому при коэффициенте 0 просто пропускаем данную итерацию степени

from random import randint

# Без словаря
def CreatePolynomial1(k):
    a = randint(-100, 100)
    s = f'{a}x**{k} '
    
    if k == 1:
        if a == 0:
            s = f'{randint(-100,100)} = 0\nБИНГО, если это верное равенство! Ставлю сотку, что нет :))' 
        else:
            s = f'{a}x + ({randint(-100,100)}) = 0'

        return s
       

    for i in range(k - 1, 1, -1):
        a = randint(-100, 100)
        
        if i > 1:    
            if a != 0:
                if a > 0:
                    s += f'+ {a}x**{i} '
                elif a == 0: 
                    s += ''
                else:
                    s += f'- {-a}x**{i} '

    a = randint(-100, 100)

    if a > 0:
        s += f'+ {a}x '
    elif a == 0:
        s += ''
    else:
        s += f'- {-a}x '

    a = randint(-100, 100)
    
    if a > 0:
        s += f'+ {a} = 0'
    elif a == 0:
        s += ''
    else:
        s += f'- {-a} = 0'
    
    return s

# Со словарём
def CreatePolynomial2(k):
    dict1 = {}
    result = f"{randint(-100, 100)}x**{k} "

    for i in range(k-1, -1, -1):
        dict1[i] = randint(-100, 100)
    
    for i in dict1.items():
        if i[1] > 0:
            result += f"+ {i[1]}x**{i[0]} " 
        elif i[1] < 0:
            result += f"- {-i[1]}x**{i[0]} " 
        
    result += "= 0"
    result = result.replace('x**1', 'x').replace('x**0', '') 

    return result

k = int(input('Please, input the highest degree of a polynomial (> 0): '))

if k <= 0:
    print("Bro, I asked you not to do this...")
    exit()

result = CreatePolynomial2(k)
print(result)

with open ('homework/seminar04_hw/task4_file.txt', 'w') as f:
    f.write(result)


    