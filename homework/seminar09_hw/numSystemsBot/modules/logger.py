import datetime as dt

def log_txt(data: str):
    time_format = "%Y-%m-%d %H:%M:%S"
    now = dt.datetime.now()
    with open('data/data.txt', 'a', encoding='utf-8') as f:
        f.write(f'{now:{time_format}}: {data}')

