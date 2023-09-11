import random
import time

choseofbot = ["камінь", "папір", "ножніці"]

while True:
    chose = input("виберіть камінь, ножиці чи папір закінчити гру exit: ")
    
    if chose.lower() == 'exit':
        print("Гра закінччилася.")
        break
    
    bot_choices = ['камінь', 'ножиці', 'папір']
    bot = random.choice(bot_choices)
    
    if chose == bot:
        print("Нічія")
    elif chose == "камінь":
        if bot == "ножиці":
            print("Ви виграли")
        else:
            print("Ви програли")
    elif chose == "ножиці":
        if bot == "папір":
            print("Ви виграли")
        else:
            print("Ви програли")
    elif chose == "папір":
        if bot == "камінь":
            print("Ви виграли")
        else:
            print("Ви програли")
    else:
        print("Некоректний вибір. Спробуйте ще раз.")
        time.sleep(0.5)


