import telebot
from telebot import types
from modules import logger as log
from modules import botMessages as bM
from modules import models

bot = telebot.TeleBot('Здесь был id бота. Убрал на всякий случай)) Вероятно, паранойя)')

@bot.message_handler(commands=["start", "старт"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    itembtn1 = types.KeyboardButton('/старт')
    itembtn2 = types.KeyboardButton('/хэлп')
    itembtn3 = types.KeyboardButton('/пэсню')
    itembtn4 = types.KeyboardButton('/картынку')
    itembtn5 = types.KeyboardButton('/арт')
    markup.row(itembtn5, itembtn4, itembtn3)
    markup.row(itembtn1, itembtn2)
    gif = open('data/logos/01.gif', 'rb')
    bot.send_video(message.chat.id, gif)
    bot.send_message(message.chat.id, bM.startM, reply_markup=markup)
    log.log_txt(f'[id: {message.from_user.id}] \
[firstName: {message.from_user.first_name}] \
[secondName: {message.from_user.last_name}] \
[userName: {message.from_user.username}] \
[request: {message.text}] \
[response: Приветствие]\n')


@bot.message_handler(commands=["help", "хелп", "хэлп"])
def start(message):
    bot.send_message(message.chat.id, bM.helpM1)
    bot.send_message(message.chat.id, bM.helpM2)
    log.log_txt(f'[id: {message.from_user.id}] \
[firstName: {message.from_user.first_name}] \
[secondName: {message.from_user.last_name}] \
[userName: {message.from_user.username}] \
[request: {message.text}] \
[response: Помощь]\n')


@bot.message_handler(commands=["пэсню", "song", "песню"])
def songs(message):
    song = models.songChoose()
    songPath = open(f'data/songs/{song}', 'rb')    
    bot.send_audio(message.chat.id, songPath)
    log.log_txt(f'[id: {message.from_user.id}] \
[firstName: {message.from_user.first_name}] \
[secondName: {message.from_user.last_name}] \
[userName: {message.from_user.username}] \
[request: {message.text}] \
[response: {song}]\n')
    
    
@bot.message_handler(commands=["картынку", "картинку", "picture", "pic"])
def pics(message):
    pic = models.picChoose()
    picPath = open(f'data/pics/{pic}', 'rb')    
    bot.send_photo(message.chat.id, picPath)
    log.log_txt(f'[id: {message.from_user.id}] \
[firstName: {message.from_user.first_name}] \
[secondName: {message.from_user.last_name}] \
[userName: {message.from_user.username}] \
[request: {message.text}] \
[response: {pic}]\n')
    

@bot.message_handler(commands=["art", "арт"])
def arts(message):
    art = models.artChoose()
    artPath = open(f'data/arts/{art}', 'rb')
    bot.send_photo(message.chat.id, artPath)
    log.log_txt(f'[id: {message.from_user.id}] \
[firstName: {message.from_user.first_name}] \
[secondName: {message.from_user.last_name}] \
[userName: {message.from_user.username}] \
[request: {message.text}] \
[response: {art}]\n')  
    

@bot.message_handler(content_types=["voice"])
def voices(message):
    voice = models.voiceChoose()
    voicePath = open(f'data/voices/{voice}', 'rb')    
    bot.send_voice(message.chat.id, voicePath)
    log.log_txt(f'[id: {message.from_user.id}] \
[firstName: {message.from_user.first_name}] \
[secondName: {message.from_user.last_name}] \
[userName: {message.from_user.username}] \
[request: userVoice] \
[response: {voice}]\n')
    
    
@bot.message_handler(func=lambda m: True )
def text_message(message):
        nList = str(message.text).split('.')
       
        if len(nList) != 2:
            bot.reply_to(message, f'Карповна!!! Чё-то ты не то вводишь! 😠')
            log.log_txt(f'[id: {message.from_user.id}] \
[firstName: {message.from_user.first_name}] \
[secondName: {message.from_user.last_name}] \
[userName: {message.from_user.username}] \
[request: {message.text}] \
[response: Ошибка ввода]\n')

        elif nList[0].isdigit() and nList[1].isdigit():
            nList[0] = int(nList[0])  # type: ignore
            nList[1] = int(nList[1])  # type: ignore
            n1 = nList[0]
            n2 = nList[1]
            result = ''
            act = ""
            while nList[0] > 0:
                if 9 < nList[0] % nList[1] < 36:
                    act += f"{nList[0]} : {nList[1]} = {nList[0]//nList[1]} ({nList[0]%nList[1]} = {models.symbs[nList[0] % nList[1]]})\n"
                    result = f"{models.symbs[nList[0] % nList[1]]}{result}"
                    nList[0] //= nList[1]  # type: ignore                    
                else:
                    act += f"{nList[0]} : {nList[1]} = {nList[0]//nList[1]} ({nList[0]%nList[1]})\n"
                    result = f"{nList[0] % nList[1]}{result}"
                    nList[0] //= nList[1]  # type: ignore
            if nList[1] > len(bM.small):
                bot.reply_to(message, f"Ок, Манюня Карповна! Ща всё решим 😎:\n\n{act}\n{n1} (в 10-ичной) = {result} (в {n2}-ичной)     👍")                
            else:
                for i in range(len(bM.small)):
                    if nList[1] == i:
                        bot.reply_to(message, f"Ок, Манюня Карповна! Ща всё решим 😎:\n\n{act}\n{n1}₁₀ = {result}{bM.small[i]}     👍")
                        break
            log.log_txt(f'[id: {message.from_user.id}] \
[firstName: {message.from_user.first_name}] \
[secondName: {message.from_user.last_name}] \
[userName: {message.from_user.username}] \
[request: {message.text}] \
[response: {n1} (10) = {result} ({n2})]\n')

        else:
            bot.reply_to(message, f'Карповна!!! Чё-то ты не то вводишь! 😬')
            log.log_txt(f'[id: {message.from_user.id}] \
[firstName: {message.from_user.first_name}] \
[secondName: {message.from_user.last_name}] \
[userName: {message.from_user.username}] \
[request: {message.text}] \
[response: Ошибка ввода]\n')


bot.polling(none_stop=True, interval=0)
