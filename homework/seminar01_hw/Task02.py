# Напишите программу для проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def CheckExpression(x, y, z):
    part1 = not(x or y or z)
    part2 = not x and not y and not z
    
    return part1 == part2


print ("Let's check the correctness of the expression:\n¬(X V Y V Z) = ¬X ⋀ ¬Y ⋀ ¬Z")

x = int(input('Please input a value for x: '))
y = int(input('Please input a value for y: '))
z = int(input('Please input a value for z: '))

if CheckExpression(x, y, z) == True:
    print('The statement is TRUE :)')

else:
    print('The statement is FALSE :(')



