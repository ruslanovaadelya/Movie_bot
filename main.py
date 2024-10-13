import telebot
from telebot import types
from config import TOKEN
import psycopg2


# conn = psycopg2.connect(host='localhost', database='dog', user='sad', password='2')
# cursor = conn.cursor()

# cursor.execute('create table fro(id serial primary key,name varchar,category varchar,movie varchar , time TIMESTAMP DEFAULT CURRENT_TIMESTAMP )')


bot = telebot.TeleBot(TOKEN)
movies_info = {
    "Случайные знакомые": {"image":open("75f317a562a9b5e9691670cf32fb6599.jpg" , "rb"), "description": "Успешный бизнесмен Александр, оказавшийся расчетливым дельцом, отбирал помещение у санатория для стариков, в котором работала симпатичная девушка Вера. После суда, она, не испытывающая по отношению к предпринимателю ничего кроме неприязни, решилась на отчаянный шаг и похитила его портфель с документами на землю."},
    "Бывшие": {"image":open("бывшие.jpg" , "rb"), "description": "Сериал 'Бывшие' - это российский драматический сериал, который повествует о любви, зависимости, дружбе, трудных отношениях. Каждый из героев сталкивается со своими личными проблемами и борется с прошлым, которое по-разному влияет на их настоящее."},
    "Совершенно другой": {"image":open("совершенно другой.jpg" , "rb"), "description": "Известный журналист Кенан влюбляется в девушку-прокурора Лейлу, которая расследует убийство бизнесмена от руки жестокого мстителя – второй личности самого Кенана."},
    "Супер агенты": {"image": open("супер агенты.jpg" , "rb"), "description": "В центре сюжета оказывается молодой человек со странным прозвищем Матильда. Он всегда мечтал стать секретным агентом, но пока вынужден выполнять поручения своего босса, генерального прокурора. Однажды начальник поручает ему отправиться в Дубай, чтобы найти там его дочь и вернуть ее домой."},
    "Призрак": {"image": open("призрак.jpg" , "rb"), "description": "Eshche vchera Yuriy Gordeev - ambitsioznyy aviakonstruktor i lyubimets zhenshchin - byl v shage ot svoego triumfa. No segodnya ego nikto ne vidit i ne slyshit, i konkurent po biznesu besprepyatstvenno zakryvaet ego kompaniyu."},
    "Папы против мам": {"image": open("папыпротив мам.jpeg" , "rb"), "description": "На одной лестничной клетке живут две семьи. В один прекрасный день папы объявляют бойкот мамам, а мамы в ответ противостоят папам. Причиной тому становятся накопившиеся семейные неурядицы: компьютерные игры одного, железная муштра второго, женская усталость и так далее. Заложниками ситуации становятся дети, которые вынуждены жить на два противоборствующих лагеря..."},
    "Анабель": {"image": open("анабель.jpg" , "rb"), "description": "Аннабель (англ. Annabelle) — тряпичная кукла, персонаж популярной городской легенды, которая гласит, что кукла была одержима духом или демоном."},
    "Чаки": {"image": open("«Культ_Чаки».jpg" , "rb"), "description": "В центре событий окажется молодая женщина по имени Ника тяжело переживающая самоубийство матери. Ее старшая сестра Барбара — властная, волевая женщина, — приезжает вместе с семьей к Нике, чтобы поддержать ее и уладить дела матери. Пока сестры заняты делом, малолетняя дочь Барбары находит в доме посылку пришедшую от неизвестного адресата, а в ней рыжеволосую куклу Чаки. "},
    "Астрал": {"image": open("астралл.jpg" , "rb"), "description": "Джош и Рене переезжают со своими детьми в новый дом, но не успевают толком распаковать вещи, как начинаются странные события. Необъяснимо перемещаются предметы, в детской звучат странные звуки… Но в настоящий ужас приходят родители, когда их десятилетний сын Далтон впадает в кому. Все усилия врачей в больнице помочь мальчику безуспешны."}}
menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
menu.row("Мелодрамма🥰","Комедия😂 ","Ужастик😱")


user1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
user1.row("Случайные знакомые","Бывшие","Совершенно другой")
user1.row("Вернутся назад")


user2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
user2.row("Супер агенты","Призрак","Папы против мам")
user2.row("Вернутся назад")


user3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
user3.row("Анабель","Чаки","Астрал")
user3.row("Вернутся назад")
@bot.message_handler(commands=['start'])

def start(message):
    bot.send_message(message.chat.id,"Приветствую в кинотеатре,выберите что хотите посмотреть.",reply_markup=menu)

@bot.message_handler(func=lambda message:True)
def second(message):
    if message.text == "Вернуться назад":
        bot.send_message(message.chat.id, "Вернемся назад", reply_markup=menu)
    elif message.text in ["Мелодрамма🥰", "Комедия😂", "Ужастик😱"]:
        if message.text == "Мелодрамма🥰":
            bot.send_message(message.chat.id, "Доступные фильмы, выберите", reply_markup=user1)
        elif message.text == "Комедия😂":
            bot.send_message(message.chat.id, "Доступные фильмы, выберите", reply_markup=user2)
        elif message.text == "Ужастик😱":
            bot.send_message(message.chat.id, "Доступные фильмы, выберите", reply_markup=user3)
    elif message.text in movies_info:
        movie_name = message.text
        movie_info = movies_info.get(movie_name)
        if movie_info:
            image_file_id = movie_info["image"]
            description = movie_info["description"]
            bot.send_photo(message.chat.id, image_file_id)
            bot.send_message(message.chat.id, description)

bot.polling(non_stop=True)









