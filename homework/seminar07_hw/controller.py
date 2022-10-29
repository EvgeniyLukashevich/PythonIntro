import logger
import model
import view

def mergeModules():
    view.inputString()
    exp_list = model.listFromString(model.user_string)
    
    while len(exp_list) < 2:
        view.inputError()
        view.inputString()
        exp_list = model.listFromString(model.user_string)
        logger.logging(f'{model.user_string} - Непростительная ошибка ввода')   
            
    while len(exp_list) >= 2:
        if '*' in exp_list or '/' in exp_list:
                exp_list = model.primeAction(exp_list)
        elif '+' in exp_list or '-' in exp_list:
            exp_list = model.nextAction(exp_list)
 
    model.result = exp_list[0]
    logger.logging(f'{model.user_string} = {model.result}')
    view.printResult()







