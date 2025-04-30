# proekt_control-work_Leonid-Sundukov-MF-71
import telebot
import random
import telebot
from telebot import types
token='7947832023:AAHV6dlN_TjaCUULDAsCXl8KFWqPI55-Dro'
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
	bot.send_message(message.chat.id,'Привет')
@bot.message_handler(commands=['button'])
def button_message(message):
	markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1=types.KeyboardButton("Кнопка") 																																		bot.send_message(message.chat.id,'Выберите что вам надо',reply_markup=markup)
	bot.send_message(message.chat.id,'Выберите что вам надо',reply_markup=markup)
bot.infinity_polling()

