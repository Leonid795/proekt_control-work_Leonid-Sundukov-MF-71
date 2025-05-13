import telebot
import random
import logging
from telebot import types

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = "8122671416:AAGfwP4wLrG-cPeKyv3XVrKxlklIHv99JF8"
bot = telebot.TeleBot(TOKEN)

user_data = {}

def generate_task():
    operations = ['+', '-', '*', '/']
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    op = random.choice(operations)

    if op == '/':
        num1 = num1 * num2  # обеспечение целочисленного деления

    task = f"{num1} {op} {num2}"

    if op == '+':
        answer = num1 + num2
    elif op == '-':
        answer = num1 - num2
    elif op == '*':
        answer = num1 * num2
    else:
        answer = num1 // num2

    return task, answer

def create_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton("/start"))
    keyboard.add(types.KeyboardButton("/help"))
    keyboard.add(types.KeyboardButton("/score"))
    keyboard.add(types.KeyboardButton("/stop"))
    return keyboard

def start_game(chat_id: int, username: str):
    task, answer = generate_task()
    user_data[chat_id] = {
        'task': task,
        'answer': answer,
        'score': 0,
        'username': username
    }
    bot.send_message(chat_id, f"Привет, {username}! Добро пожаловать в игру по легкой математике.", reply_markup=create_keyboard())
    bot.send_message(chat_id, f"Реши задание:\n{task}\n\nОтправь ответ числом.", reply_markup=create_keyboard())

@bot.message_handler(commands=['start'])
def start_handler(message):
    chat_id = message.chat.id
    username = message.from_user.first_name or "игрок"
    start_game(chat_id, username)

@bot.message_handler(commands=['help'])
def help_handler(message):
    chat_id = message.chat.id
    help_text = (
        "Я бот, который поможет тебе тренироваться в легкой математике!\n\n"
        "Используй команды:\n"
        "/start - начать игру\n"
        "/score - показать счет\n"
        "/stop - завершить игру\n\n"
        "После получения задания отправляй ответ числом."
    )
    bot.send_message(chat_id, help_text, reply_markup=create_keyboard())

@bot.message_handler(commands=['score'])
def score_handler(message):
    chat_id = message.chat.id
    score = user_data.get(chat_id, {}).get('score', 0)
    bot.send_message(chat_id, f"Твой текущий счет: {score}", reply_markup=create_keyboard())

@bot.message_handler(commands=['stop'])
def stop_handler(message):
    chat_id = message.chat.id
    if chat_id in user_data:
        del user_data[chat_id]
    bot.send_message(chat_id, "Игра остановлена. Если хочешь сыграть снова, отправь /start.", reply_markup=create_keyboard())

@bot.message_handler(func=lambda message: True)
def answer_handler(message):
    chat_id = message.chat.id
    text = message.text.strip()

    if chat_id not in user_data:
        bot.send_message(chat_id, "Пожалуйста, начни игру командой /start.", reply_markup=create_keyboard())
        return

    if not (text.lstrip('-').isdigit()):
        bot.send_message(chat_id, "Пожалуйста, отправь числовой ответ.", reply_markup=create_keyboard())
        return

    user_answer = int(text)
    correct_answer = user_data[chat_id]['answer']

    if user_answer == correct_answer:
        user_data[chat_id]['score'] += 1
        score = user_data[chat_id]['score']
        bot.send_message(chat_id, f"Верно! 🎉 Твой счет: {score}", reply_markup=create_keyboard())
        task, answer = generate_task()
        user_data[chat_id]['task'] = task
        user_data[chat_id]['answer'] = answer
        bot.send_message(chat_id, f"Новое задание:\n{task}\nОтправь ответ числом.", reply_markup=create_keyboard())
    else:
        bot.send_message(chat_id, f"Неверно. Попробуй еще раз.\nЗадание: {user_data[chat_id]['task']}", reply_markup=create_keyboard())

if __name__ == '__main__':
    logger.info("Бот запущен!")
    bot.infinity_polling()
