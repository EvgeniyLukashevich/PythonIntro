import datetime

def logging(data: str):
    time_format = "%Y-%m-%d %H:%M:%S"
    now = datetime.datetime.now()     
    with open ('homework\seminar07_hw\log.txt', 'a', encoding="utf-8") as f:
        f.write(f'{now:{time_format}} : {data}\n')