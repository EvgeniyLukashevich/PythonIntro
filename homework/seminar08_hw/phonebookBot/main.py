import telebot
from telebot import types
import logger as log
import botMessages as bM
import models

bot = telebot.TeleBot('5656676373:AAFwnluOWRO0bmF10BGaq4LQZFLFqoRYaSo')

@bot.message_handler(commands=["start", "старт"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    itembtn1 = types.KeyboardButton(models.getButtons()[3])
    itembtn2 = types.KeyboardButton(models.getButtons()[4])
    itembtn3 = types.KeyboardButton(models.getButtons()[0])
    itembtn4 = types.KeyboardButton(models.getButtons()[1])
    markup.row(itembtn3, itembtn4)
    markup.row(itembtn1, itembtn2) 
    bot.send_message(message.chat.id, bM.start_message, reply_markup=markup)
    log.log_txt(f'[id: {message.from_user.id}] \
[firstName: {message.from_user.first_name}] \
[secondName: {message.from_user.last_name}] \
[userName: {message.from_user.username}] \
[request: {message.text}]\n')


@bot.message_handler(func=lambda m: m.text == models.getButtons()[0])
def addContact(message):
    bot.send_message(message.chat.id, "✏ ВВЕДИ ИМЯ КОНТАКТА")
    log.log_txt(f'[id: {message.from_user.id}] \
[firstName: {message.from_user.first_name}] \
[secondName: {message.from_user.last_name}] \
[userName: {message.from_user.username}] \
[request: {message.text}]\n')
    bot.register_next_step_handler(message, addName)
def addName(message):
    models.setName(message.text)
    bot.send_message(message.chat.id, "✏ ВВЕДИ НОМЕР")
    bot.register_next_step_handler(message, addNumber)
def addNumber(message):
    models.setNumber(message.text)
    bot.send_message(message.chat.id, "✏ ВВЕДИ КОММЕНТАРИЙ")
    bot.register_next_step_handler(message, addComment)
def addComment(message):
    models.setComment(message.text)
    log.addData(message.from_user.id)
    bot.send_message(message.chat.id, "КОНТАКТ УСПЕШНО ДОБАВЛЕН ✅")
    models.resetVariables()



@bot.message_handler(func=lambda m: m.text == models.getButtons()[4])
def sendFile(message):
    bot.send_message(message.chat.id, "ЛОВИ СВОЙ ФАЙЛ:")
    bot.send_document(message.chat.id, log.sendData(message.from_user.id))
    log.log_txt(f'[id: {message.from_user.id}] \
[firstName: {message.from_user.first_name}] \
[secondName: {message.from_user.last_name}] \
[userName: {message.from_user.username}] \
[request: {message.text}]\n')


@bot.message_handler(func=lambda m: m.text == models.getButtons()[3])
def showContacts(message):
    models.setDictionary(message.from_user.id)
    bot.send_message(message.chat.id, models.messageFromDictionary(models.getDictionary()))
    log.log_txt(f'[id: {message.from_user.id}] \
[firstName: {message.from_user.first_name}] \
[secondName: {message.from_user.last_name}] \
[userName: {message.from_user.username}] \
[request: {message.text}]\n')


@bot.message_handler(func=lambda m: m.text == models.getButtons()[1])
def rewriteContact(message):
    bot.send_message(message.chat.id, "Введи id-номер контакта, который хочешь изменить и что ты хочешь изменить (например: 5 имя)")
    log.log_txt(f'[id: {message.from_user.id}] \
[firstName: {message.from_user.first_name}] \
[secondName: {message.from_user.last_name}] \
[userName: {message.from_user.username}] \
[request: {message.text}]\n')
    bot.register_next_step_handler(message, check)
def check(message):
    models.rewriteContact(message.text)
    bot.send_message(message.chat.id, "Введи верное значение")
    bot.register_next_step_handler(message, changing)
def changing(message):
    models.setDictionary(message.from_user.id)
    if models.rewriteVar == "имя":
        models.getDictionary()[int(models.rewriteId)][0] = f" {message.text}"
        bot.send_message(message.chat.id, "КОНТАКТ УСПЕШНО ИЗМЕНЁН ✅")
        log.dataUpdate(message.from_user.id)
    elif models.rewriteVar == "номер":
        models.getDictionary()[int(models.rewriteId)][1] = f" {message.text}"
        bot.send_message(message.chat.id, "КОНТАКТ УСПЕШНО ИЗМЕНЁН ✅")
        log.dataUpdate(message.from_user.id)
    elif models.rewriteVar == "комментарий":
        models.getDictionary()[int(models.rewriteId)][2] = f" {message.text}"
        bot.send_message(message.chat.id, "КОНТАКТ УСПЕШНО ИЗМЕНЁН ✅")
        log.dataUpdate(message.from_user.id)
    else:
        bot.send_message(message.chat.id, "ОШИБКА ВВОДА❌")


bot.polling(none_stop=True, interval=0)