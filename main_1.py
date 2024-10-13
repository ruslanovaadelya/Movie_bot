import telebot
from telebot import types
import psycopg2
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
menu.row("Мелодрамма🥰", "Комедия😂", "Ужастик😱")

user1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
user1.row("Случайные знакомые", "Бывшие", "Совершенно другой")

user2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
user2.row("Супер агенты", "Призрак", "Папы против мам")

user3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
user3.row("Анабель", "Чакки", "Астралл")

categories = {
    "Мелодрамма🥰": user1,
    "Комедия😂": user2,
    "Ужастик😱": user3
}

def create_table():
    conn = psycopg2.connect(host='localhost', database='dog', user='sad', password='2')
    cursor = conn.cursor()
    # cursor.execute("""
    #     CREATE TABLE IF NOT EXISTS movie_choices (
    #         id SERIAL PRIMARY KEY,
    #         name INTEGER NOT NULL,
    #         category VARCHAR(255) NOT NULL,
    #         film VARCHAR(255) NOT NULL,
    #         time_0 TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    #     )
    # """)
    conn.commit()
    cursor.close()
    conn.close()

def insert_movie_choice(user_id, username, movie_category, movie_choice):
    conn = psycopg2.connect(host='localhost', database='dog', user='sad', password='2')
    cursor = conn.cursor()
    query = "INSERT INTO movie_choices (name,category,film) VALUES (%s, %s, %s)"
    cursor.execute(query, (user_id, username, movie_category, movie_choice))
    conn.commit()
    cursor.close()
    conn.close()

@bot.message_handler(commands=['start'])
def start(message):
    create_table()
    bot.send_message(message.chat.id, "Приветствую в кинотеатре, выберите что хотите посмотреть.", reply_markup=menu)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "Вернуться назад":
        bot.send_message(message.chat.id, "Вернемся назад", reply_markup=menu)
    elif message.text in categories:
        bot.send_message(message.chat.id, "Доступные фильмы, выберите", reply_markup=categories[message.text])
    elif message.text in ["Случайные знакомые", "Бывшие", "Совершенно другой", "Супер агенты", "Призрак", "Папы против мам", "Анабель", "Чакки", "Астралл"]:
        movie_category = None
        for category, keyboard in categories.items():
            if message.text in keyboard.keyboard:
                movie_category = category
                break
        if movie_category:
            insert_movie_choice(message.from_user.id, message.from_user.username, movie_category, message.text)
            bot.send_message(message.chat.id, "Спасибо за выбор!")
        else:
            bot.send_message(message.chat.id, f"Что-то пошло не так. Категория фильма: {movie_category}")

# bot.polling()


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "Вернуться назад":
        bot.send_message(message.chat.id, "Вернемся назад", reply_markup=menu)
    elif message.text in categories:
        bot.send_message(message.chat.id, "Доступные фильмы, выберите", reply_markup=categories[message.text])
    elif message.text in ["Случайные знакомые", "Бывшие", "Совершенно другой", "Супер агенты", "Призрак", "Папы против мам", "Анабель", "Чакки", "Астралл"]:
        movie_category = None
        for category, keyboard in categories.items():
            if message.from_user.username in keyboard.keyboard:
                movie_category = category
                break
        if movie_category:
            insert_movie_choice(message.from_user.id, message.from_user.username, movie_category, message.text)
            bot.send_message(message.chat.id, "Спасибо за выбор!")
        else:
            bot.send_message(message.chat.id, f"Что-то пошло не так. Категория фильма: {movie_category}")

bot.polling()