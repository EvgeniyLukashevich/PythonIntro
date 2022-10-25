import logger

def errorMessage():
    x = "Непростительная ошибка!"
    logger.logAction(x)
    print(x)


def errorNull():
    x = "Непростительная ошибка! Не дели на ноль, пожалуйста :)"
    logger.logAction(x)
    print(x)


def inputNum():
    x = input('Введите число: ')
    
    while x.isdigit() == False:
        errorMessage()
        x = input('Введите число: ')
    
    return int(x)


def inputOperation():
    x = input('Введите действие: ')
    
    while x not in ['+', '-', '*', 'x', '/', ':', '=']:
        errorMessage()
        x = input('Введите действие: ')
    
    return x


def printResult(result):
    print(f'Результат: {result}')


def printFinallyResult(result):
    print(f'Итоговый результат: {result}')