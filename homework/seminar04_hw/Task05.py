# TASK 5. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов


def EquationsSum(eq1, eq2):
    eq1 = eq1.replace(' + ', ' +').replace(' - ', ' -')
    eq2 = eq2.replace(' + ', ' +').replace(' - ', ' -')

    eq1 = eq1.split()
    eq2 = eq2.split()

    eq1 = eq1[:-2]
    eq2 = eq2[:-2]

    dictEq1 = {}
    dictEq2 = {}
    dictEq3 = {}

    for i in range(len(eq1)):
        eq1[i] = eq1[i].replace('+', '').split('x**')
        dictEq1[int(eq1[i][1])] = int(eq1[i][0])

    for i in range(len(eq2)):
        eq2[i] = eq2[i].replace('+', '').split('x**')
        dictEq2[int(eq2[i][1])] = int(eq2[i][0])

    for i in dictEq1.keys():
        dictEq3[i] = dictEq1[i] + dictEq2[i]

    return dictEq3


def CreatePolynomial(equationDict):
    result = ''
    first = True

    for i in equationDict.items():
        if first:
            result += f"{i[1]}x**{i[0]} " 
            first = False
            continue

        if i[1] > 0:
            result += f"+ {i[1]}x**{i[0]} " 
        elif i[1] < 0:
            result += f"- {-i[1]}x**{i[0]} "
        
    result += "= 0"
    result = result.replace('x**1', 'x').replace('x**0', '') 

    return result


with open ('homework/seminar04_hw/task5_file1.txt') as f:
    equation1 = f.readline()

with open ('homework/seminar04_hw/task5_file2.txt') as f:
    equation2 = f.readline()

sumOfEquations = EquationsSum(equation1, equation2)
result = CreatePolynomial(sumOfEquations)

print(result)

with open ('homework/seminar04_hw/task5_file3.txt', 'w') as f:
    f.write(result)