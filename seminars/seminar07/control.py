import view
import models
import logger


def firstClick():
    global number1
    global number2
    number1 = view.inputNum()
    operation = view.inputOperation()
    number2 = view.inputNum()
    
    while (operation == '/' or operation == ':') and number2 == 0:
        view.errorNull()
        number2 = view.inputNum()
    
    return operation

def nextClick():
    global number3
    operation = view.inputOperation()
    if operation == '=': return False
    number3 = view.inputNum()
    
    while (operation == '/' or operation == ':') and number3 == 0:
        view.errorNull()
        number3 = view.inputNum()
    
    return operation


def checkFirstOperation(operation):
    if operation == '+': 
        return models.actionSum(number1, number2)
    
    elif operation == '-': 
        return models.actionDiff(number1, number2)
    
    elif operation == '*' or operation == 'x': 
        return models.actionMult(number1, number2)
    
    elif operation == '/' or operation == ':': 
        return models.actionDiv(number1, number2)


def checkNextOperation(operation, result):
    if operation == '+': 
        return models.actionSum(result, number3)
    
    elif operation == '-': 
        return models.actionDiff(result, number3)
    
    elif operation == '*' or operation == 'x': 
        return models.actionMult(result, number3)
    
    elif operation == '/' or operation == ':': 
        return models.actionDiv(result, number3)

        


def start():
    first_operation = firstClick()
    first_result = checkFirstOperation(first_operation)
    logger.logAction(f'{number1} {first_operation} {number2} = {first_result}')
    view.printResult(first_result)
    second_operation = nextClick()
    
    if second_operation == False:
        logger.logAction(f"Your finally result is {first_result}")
        view.printFinallyResult(first_result)
        return ""
    
    next_result = checkNextOperation(second_operation, first_result)
    logger.logAction(f'{first_result} {second_operation} {number3} = {next_result}')    
    view.printResult(next_result)
    
    while True:    
        next_operation = nextClick()
        
        if next_operation == False:
            logger.logAction(f"Your finally result is {next_result}")
            view.printFinallyResult(next_result)
            break
        
        temp_Result = next_result
        next_result = checkNextOperation(next_operation, next_result)
        logger.logAction(f'{temp_Result} {next_operation} {number3} = {next_result}')
        view.printResult(next_result)
        
