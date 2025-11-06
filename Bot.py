import telebot
from telebot import types
from config import BOT_TOKEN
import datetime
import sqlite3  
import os    
from database import create_database, add_user,get_user,get_all_users,get_users_count


bot = telebot.TeleBot(BOT_TOKEN)
print("стартовый запуск есть, гнида!")


@bot.message_handler(commands=["help"])
def say_poshel_naxui(message):
    try:
        with open ("media\interny.mp4",'rb') as video:
            bot.send_video(
                message.chat.id,
                video,
                caption="ТЫ БЕЗМОЗГЛАЯ ИНФУЗОРИЯ РАЗДУТАЯ САМОМНЕНИЕМ, БЕЗРУКИЙ ЭМБРИОН С КРАСНЫМ ДИПЛОМОМ!",
                parse_mode="Markdown",
                supports_streaming=True
            )
    except FileNotFoundError:
        bot.reply_to(message,"ПАШЕЛ НАХУЙ ВИДЕВА НЕ ГРУЗИТСЯ ЧЕТА")


def create_keyboard_buttons():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    b1=types.KeyboardButton("Контакты")
    b2=types.KeyboardButton("Пожертвовать лоху")
    b3=types.KeyboardButton("Кто я такой?")
    b4=types.KeyboardButton("хочешь, покажу пенис?")
    
    keyboard.add(b1,b2)
    keyboard.add(b3,b4)
    
    return keyboard 

def create_inlines():
    keyboard =types.InlineKeyboardMarkup()
    
    button1 = types.InlineKeyboardButton("Ссылка на мое портфолио: ",url="https://ru.wikipedia.org/wiki/")
    button2 = types.InlineKeyboardButton("Планы на будушее: ",callback_data="plans")
    button3 = types.InlineKeyboardButton("Мои достижения: ",callback_data="achive")
    button4 = types.InlineKeyboardButton("Дополнительная кнопка",callback_data="attention")
    
    keyboard.add(button1,button2)
    keyboard.add(button3,button4)
    
    return keyboard



@bot.callback_query_handler(func=lambda call: True)
def handle_inline_buttons(call):
    if call.data == "achive":
        bot.answer_callback_query(call.id, "coming soon...")
    elif call.data == "plans":
        bot.answer_callback_query(call.id, "Много...")
    elif call.data == "attention":
        bot.answer_callback_query(call.id, "ЭТА КНОПКА В РАЗРАБОТКЕ", show_alert=True)
        

@bot.message_handler(commands=['start'])
def say_hello(message):
    chat_id = message.chat.id
    bot.send_message(chat_id,"здарова, чепуха",reply_markup=create_keyboard_buttons())
    
@bot.message_handler(commands=['getid'])
def get_chat_id(message):
    chat_id = message.chat.id
    bot.reply_to(message, f"ID этого чата: {chat_id}")
    
@bot.message_handler(content_types=["text"])
def answers(message):
    if message.text == "Контакты":
        bot.reply_to(message,"Контакты владельца @Shkiper004")
    elif message.text == "Пожертвовать лоху":
        bot.reply_to(message,"Реквизиты будут добавлены позже...")
    elif message.text == "Кто я такой?":
        bot.reply_to(message,"Информация будет дополнена позже")
    elif message.text == "хочешь, покажу пенис?":
        bot.reply_to(message,"го")
        bot.send_message(message.chat.id, "Держи инлайн-кнопки:", reply_markup=create_inlines())
    # Убери отсюда bot.send_message - он выполняется после ЛЮБОГО текста!
        
@bot.message_handler(content_types=["voice"])
def answer_bad(message):
    bot.reply_to(message,"Извини, я пока не понимаю голосовые сообщения(")
    
@bot.message_handler(content_types=["photo"])
def answer_bad(message):
    bot.reply_to(message,"Извини, я пока не распознаю фотографии(")
    
      
bot.polling()