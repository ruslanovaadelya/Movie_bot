# import telebot
# from telebot import types
# from config import TOKEN

# bot = telebot.TeleBot(TOKEN)

# menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
# menu.row("Мелодрамма🥰","Комедия😂 ","Ужастик😱")


# user1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
# user1.row("Случайные знакомые","Бывшие","Совершенно другой")
# user1.row("Вернутся назад")


# user2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
# user2.row("Супер агенты","Призрак","Папы против мам")
# user2.row("Вернутся назад")


# user3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
# user3.row("Анабель","Чакки","Астралл")
# user3.row("Вернутся назад")

# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.send_message(message.chat.id,"Приветствую в кинотеатр,выберите что хотите посмотреть.",reply_markup=menu)

# @bot.message_handler(func=lambda message:True)
# def second(message):
#     if message.text == "Мелодрамма":
#         bot.send_message(message.chat.id, "доступные кино, выберите",reply_markup=user1)
#     elif message.text == "Случайные знакомые":
#             bot.send_photo(message.chat.id,"Мелодрамма интересная")
#     elif message.text == "Бывшие":
#             bot.send_message(message.chat.id,"Тоже мелодрамма вроде тоже норм")
#     elif message.text == "Совершенно другой":
#             bot.send_message(message.chat.id,"Мелодрамма после просмотра будут сопли")
    
    
    
#     elif message.text == "Комедия":
#         bot.send_message(message.chat.id, "доступные кино, выберите",reply_markup=user2)
#     if message.text == "Супер агенты":
#             bot.send_photo(message.chat.id," Нормальное кино")
#     elif message.text == "Призрак":
#             bot.send_message(message.chat.id," вроде тоже норм")
#     elif message.text == "Папы против мам":
#             bot.send_message(message.chat.id," после просмотра будут сопли потому что будете много смеяться")
          

#     elif  message.text == "Ужастик":
#         bot.send_message(message.chat.id, "доступные кино, выберите",reply_markup=user3)
#     elif message.text == "Анабель":
#             bot.send_photo(message.chat.id,"интересный ужастик не очень ужасный")
#     elif message.text == "Чакки":
#             bot.send_message(message.chat.id,"Ну не знаю ,что за вкус у тебя")
#     elif message.text == "Астралл":
#             bot.send_message(message.chat.id,"после просмотра вы обосретесь")
#     elif message.text == "Вернутся в назад":
#             bot.send_message(message.chat.id, "Вернемся назад",reply_markup=menu)         




# bot.polling(non_stop=True)