import telebot
from info import my_information, contacts


token = 'Your Token'
bot = telebot.TeleBot(token)


help_message = (
    """ Я умею:
/help - узнать мои возможности
/about - расскажу о себе
/contacts - способы со мной связаться""")


@bot.message_handler(commands=['start'])
def command_start(message):
    bot.send_message(message.chat.id, text=f'Здравствуй, {message.from_user.first_name}.' + help_message)


@bot.message_handler(commands=['help'])
def command_help(message):
    bot.send_message(message.chat.id, text=help_message)


@bot.message_handler(commands=['about'])
def command_about(message):
    bot.send_message(message.chat.id, text=my_information)
    bot.send_photo(message.chat.id, open('photo_2023-12-18_18-21-22.jpg', 'rb+'))


@bot.message_handler(commands=['contacts'])
def bot_contacts(message):
    bot.send_message(message.chat.id, text=contacts)


@bot.message_handler(content_types=['text'])
def repeat_message(message):
    bot.send_message(message.chat.id, f'Пока я не умею обрабатывать присланное вами сообщение."{message.text}", '
                                      f'пожалуйста используйте команды(посмотреть команды - /help)')


bot.polling()
