# proekt_control-work_Leonid-Sundukov-MF-71
proekt_control-work_Leonid(Sundukov)MF-71
import telebot
import random
ef generate_problem(difficulty):
    if difficulty == 'easy':
        a, b = random.randint(1, 10), random.randint(1, 10)
        return f"{a} + {b} = ?", a + b
    elif difficulty == 'medium':
        a, b = random.randint(10, 50), random.randint(1, 20)
        return f"{a} - {b} = ?", a - b
