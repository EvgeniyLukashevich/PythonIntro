import logger
import model



def inputError():
    # logger.logger('Ошибка ввода данных')
    return print('Ошибка ввода данных')

def inputString():
    model.user_string = input('Введите строку для вычисления: ')

def printResult():
    return print(f'Результат: {model.result}')