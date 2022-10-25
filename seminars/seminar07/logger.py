import datetime


def logAction(data: str):
    time_format = "%Y-%m-%d %H:%M:%S"
    now = datetime.datetime.now()
    
    with open ('seminars\seminar07\log.csv', 'a', encoding="utf-8") as f:
        f.write(f'{now:{time_format}};{data}\n')
    
    with open ('seminars\seminar07\log.txt', 'a', encoding="utf-8") as f:
        f.write(f'{now:{time_format}} : {data}\n')
    

