import logger

human_name = ""
phone_number = ""
human_comment = ""
buttons = ["Добавить Контакт", "Изменить Контакт", "Удалить Контакт", 
"Показать Контакты", "Дай Файлик", "Найти Контакт"]
dictionary = {}
rewriteId = ""
rewriteVar = ""

def rewriteContact(text: str):
    global rewriteId
    global rewriteVar
    text = text.split()
    rewriteId = text[0]
    rewriteVar = text[1]




def setDictionary(user_id):
    global dictionary
    with open(f'homework\seminar08_hw\phonebookBot\data\{user_id}_phonebook.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            list = line.strip().split(":")
            dictionary[int(list[0].strip())] = list[1].split(" || ")

def getDictionary():
    global dictionary
    return dictionary

def messageFromDictionary(dictionary: dict):
    a = ""
    for key in dictionary:
        a = a + f"{key} : {dictionary[key][0]} - {dictionary[key][1]} ({dictionary[key][2]})\n"
    return a


def resetVariables():
    global human_name
    global phone_number
    global human_comment
    human_name = ""
    phone_number = ""
    human_comment = ""


def setName(user_message: str):
    global human_name
    human_name = user_message

def setNumber(user_message: str):
    global phone_number
    phone_number = user_message

def setComment(user_message: str):
    global human_comment
    human_comment = user_message


def getName():
    global human_name
    return human_name

def getNumber():
    global phone_number
    return phone_number

def getComment():
    global human_comment
    return human_comment

def getButtons():
    global buttons
    return buttons




