import random
import telebot
from telebot import types
import config
bot = telebot.TeleBot(config.TOKEN)
a = random.randint()

@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item = types.KeyboardButton('рандомное число')
    item1 = types.KeyboardButton('игра')
    item2 = types.KeyboardButton('фильм')
    item3 = types.KeyboardButton('музыка')
    item4 = types.KeyboardButton('обои')
    markup.add(item1,item2,item,item3,item4)
  
    bot.send_message(message.chat.id,
        "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный Актаном чтобы быть помогать вам.".format(
                message.from_user, bot.get_me()),
                parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь и напиши /help.?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    elif  message.text == "игра":
        bot.send_message(message.from_user.id,  "https://www.cartoonnetworkhq.com/games")
    elif message.text == "фильм":
        bot.send_message(message.from_user.id,  "www.kinopoisk.ru/film/8124/")
    elif message.text == "музыка":
        bot.send_message(message.from_user.id,  "https://muzati.net/" )
    elif message.text == "обои": 
        bot.send_message(message.from_user.id,  "https://ru.wallpaper.mob.org/" )
    elif message.text == "рандомное число":
        bot.send_message(message.from_user.id,    a  )
    else:
        bot.send_message(message.from_user.id,  "я тебя не понимаю нажми /start")
    

bot.polling(none_stop=True, interval=0)
