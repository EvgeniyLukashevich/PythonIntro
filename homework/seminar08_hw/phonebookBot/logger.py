import datetime as dt
import models as m



def log_txt(data: str):
    time_format = "%Y-%m-%d %H:%M:%S"
    now = dt.datetime.now()
    with open('homework\seminar08_hw\phonebookBot\log.txt', 'a', encoding='utf-8') as f:
        f.write(f'{now:{time_format}}: {data}')

def addData(user_id):
    with open(f'homework\seminar08_hw\phonebookBot\data\{user_id}_phonebook.txt', 'a+', encoding='utf-8') as f:
        line_count = sum(1 for line in open(f'homework\seminar08_hw\phonebookBot\data\{user_id}_phonebook.txt'))
        f.write(f'{line_count + 1} : {m.getName()} || {m.getNumber()} || {m.getComment()}\n')

def sendData(user_id):
    return open(f'homework\seminar08_hw\phonebookBot\data\{user_id}_phonebook.txt', 'rb')


def dataUpdate(user_id):
    with open(f'homework\seminar08_hw\phonebookBot\data\{user_id}_phonebook.txt', 'w+', encoding='utf-8') as f:
        for key in m.getDictionary():
            f.write(f'{key} : {m.getDictionary()[key][0].strip()} || {m.getDictionary()[key][1].strip()} || {m.getDictionary()[key][2].strip()}\n')



