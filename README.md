# proekt_control-work_Leonid-Sundukov-MF-71
import telebot
import random
from telebot import types
token='7947832023:AAHV6dlN_TjaCUULDAsCXl8KFWqPI55-Dro'
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
	bot.send_message(message.chat.id,'Привет')
@bot.message_handler(commands=['button'])
def button_message(message):
	markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1=types.KeyboardButton("Кнопка") 																																		
	bot.send_message(message.chat.id,'Выберите что вам надо',reply_markup=markup)
bot.infinity_polling()
import math
def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operation = random.choice(['+', '-', '*'])
def question(update: Update, context: CallbackContext) -> None:
    question_text, answer = generate_question()
    context.user_data['answer'] = answer  # Сохраняем правильный ответ
    update.message.reply_text(question_text)
