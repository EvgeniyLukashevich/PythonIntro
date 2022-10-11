# TASK 1. Вычислить число c заданной точностью *d*

from math import pi 

# Метод без округления
def Accurate1(num, d):
    result = ''
    num = str(num)
    d = str(d)

    for i in range(len(d)):
        result = result + num[i]
    
    return float(result)

# Метод с округлением
def Accurate2(num, d):
    d = str(d)
    roundNum = 0

    for i in range(len(d) - 1, 0, -1):
        if d[i] == '.': break
        roundNum += 1
    
    return round(num, roundNum)
    

d = float(input('Please, input d (from 0.1 to 0.0000000001): '))

if d >= 1 or d < 0.0000000001:
    print('Bro... Your d must be beetween 0.1 and 0.0000000001')
    exit()

num = Accurate2(pi, d)

print(f'Catch your pi-number: {num}')