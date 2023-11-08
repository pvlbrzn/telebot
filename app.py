import telebot
from telebot import types


token = "6948551589:AAEwvxP47DRSJGYmlnOFVnZvK1hvc1MIExw"
bot = telebot.TeleBot(token)


# it's function for command "/start"
@bot.message_handler(commands=["start"])
def start(message):
    mess = f"Привет, <b>{message.from_user.first_name} </b> ✌️"
    bot.send_message(message.chat.id, mess, parse_mode="html")


# it's function tracking text entered by the user
@bot.message_handler(content_types=["text"])
def get_user_text(message):
    if message.text == "Привет":
        bot.send_message(message.chat.id, "И тебе привет!!!")
    elif message.text == "id":
        bot.send_message(message.chat.id, f"Твой ID: {message.from_user.id}")
    elif message.text == "фото":
        with open("barni.jpg", "rb") as photo:
            bot.send_photo(message.chat.id, photo)
    else:
        bot.send_message(
            message.chat.id, "Я тебя не понимаю😵‍💫. Паша сделал меня глупым Ботом 👶"
        )


# it's function tracking photo sent by the user
@bot.message_handler(content_types=["photo"])
def ger_user_photo(message):
    bot.send_message(message.chat.id, "Вау, крутая фотогорафия!!!")


@bot.message_handler(commands=["website"])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton(
            "Посетить инстаграм разработчика этого шедевра",
            url="https://instagram.com/berezan_15?igshid=bncyYjFoa3pzeWxp&utm_source=qr",
        )
    )
    bot.send_message(message.chat.id, "Перейдите в инстаграм", reply_markup=markup)


# @bot.message_handler(commands=["help"])
# def website(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
#     website = types.KeyboardButton("Website")
#     start = types.KeyboardButton("Start")
#     markup.add(website, start)
#     bot.send_message(message.chat.id, "Перейдите в инстаграм", reply_markup=markup)


bot.polling(none_stop=True)
