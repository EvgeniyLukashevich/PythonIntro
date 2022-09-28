# Напишите программу, которая принимает на вход координаты
# двух точек и находит расстояние между ними в 2D пространстве.

def TwoPointsDistance (x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2-y1)**2)**0.5

x1 = int(input('Please input x-value of 1st point: '))
y1 = int(input('Please input y-value of 1st point: '))
x2 = int(input('Please input x-value of 2nd point: '))
y2 = int(input('Please input y-value of 2nd point: '))

result = TwoPointsDistance(x1, y1, x2, y2)

print(f"The distance between A({x1}; {y1}) and B({x2}; {y2}) is {result}")