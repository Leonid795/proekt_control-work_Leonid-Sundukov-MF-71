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
ef handle_answer(update: Update, context: CallbackContext) -> None:
    user_answer = update.message.text
    correct_answer = context.user_data.get('answer')

    if correct_answer is not None:
        if user_answer.isdigit() and int(user_answer) == correct_answer:
            update.message.reply_text("Правильно! Хочешь еще одну задачу? Напиши /question.")
        else:
            update.message.reply_text(f"Неправильно. Правильный ответ: {correct_answer}. Напиши /question, чтобы попробовать еще раз.")
    else:
        update.message.reply_text("Сначала напиши /question, чтобы получить задачу.")
