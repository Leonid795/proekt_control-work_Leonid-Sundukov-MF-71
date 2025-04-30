# proekt_control-work_Leonid-Sundukov-MF-71
import telebot
import random

# Замените 'YOUR_TOKEN' на токен вашего бота
API_TOKEN = 'YOUR_TOKEN'
bot = telebot.TeleBot(API_TOKEN)

# Функция для генерации математических задач
def generate_problem(difficulty):
    if difficulty == 'easy':
        a, b = random.randint(1, 10), random.randint(1, 10)
        return f"{a} + {b} = ?", a + b
    elif difficulty == 'medium':
        a, b = random.randint(10, 50), random.randint(1, 20)
        return f"{a} - {b} = ?", a - b
    elif difficulty == 'hard':
        a, b = random.randint(1, 20), random.randint(1, 20)
        return f"{a} * {b} = ?", a * b
    else:
        return None, None
# Команда /start
  update.message.reply_text("Привет! Я математический бот. Решай задачи, которые я тебе дам!")

  question, answer = generate_question()
  context.user_data['answer'] = answer
  update.message.reply_text(question)
 Обработка текстовых сообщений
 def handle_message(update: Update, context: CallbackContext) -> None:
  user_answer = update.message.text

  if user_answer.isdigit():
  user_answer = int(user_answer)
  correct_answer = context.user_data.get('answer')

  if user_answer == correct_answer:
  update.message.reply_text("Правильно! Вот следующая задача:")
  question, answer = generate_question()
  context.user_data['answer'] = answer
  update.message.reply_text(question)
  else:
  update.message.reply_text("Неправильно. Попробуй еще раз!")
  else:
  update.message.reply_text("Пожалуйста, вводи только числа.")
   def main():
  # Замените 'YOUR_TOKEN' на токен вашего бота
  updater = Updater("YOUR_TOKEN")
  
  # Получаем диспетчер для регистрации обработчиков
  dispatcher = updater.dispatcher
    # Команды
  dispatcher.add_handler(CommandHandler("start", start))
 # Обработка текстовых сообщений
  dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
 # Запуск бота 61 updater.start_polling()
   # Ожидание завершения работы
  updater.idle()
 if __name__ == '__main__':
  main()
