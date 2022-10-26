user_string = 0
result = 0


def listFromString(string: str):
    user_list = string.replace(' ', '').strip()
    user_list = user_list.replace('+', ' + ').replace('-', ' - ')\
        .replace('*', ' * ').replace('/', ' / ').split()
    if user_list[0] in ['+', '-', '*', '/']:
        user_list.insert(0, '0')
    return user_list

def primeAction(exp_list: list):
    try:
        for i in range(len(exp_list)):
            if exp_list[i] == '/':
                exp_list[i - 1] = float(exp_list[i - 1]) / float(exp_list[i + 1])
                exp_list.pop(i)
                exp_list.pop(i)
                break
            elif exp_list[i] == '*':
                exp_list[i - 1] = float(exp_list[i - 1]) * float(exp_list[i + 1])
                exp_list.pop(i)
                exp_list.pop(i)
                break
    except:
        exp_list = ['0', '0']
    return exp_list

def nextAction(exp_list: list):
    try:
        for i in range(len(exp_list)):
            if exp_list[i] == '+':
                exp_list[i - 1] = float(exp_list[i - 1]) + float(exp_list[i + 1])
                exp_list.pop(i)
                exp_list.pop(i)
                break
            elif exp_list[i] == '-':
                exp_list[i - 1] = float(exp_list[i - 1]) - float(exp_list[i + 1])
                exp_list.pop(i)
                exp_list.pop(i)
                break
    except:
        exp_list = ['0', '0']
    return exp_list

