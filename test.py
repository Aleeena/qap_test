import telebot

TOKEN = "7408688438:AAH5ZOMqyo0zGnxtj0xEXJOctuCD954sRxw"

bot = telebot.TeleBot(TOKEN)

# content_types = audio, photo, voice, video, document, text, location, contact, sticker (основные)
# Обрабатываются все сообщения, содержащие команды '/start' or '/help'.


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f"Welcome, {message.chat.username}")


# Обрабатываются все документы и аудиозаписи
@bot.message_handler(content_types=['document', 'audio'])
def handle_docs_audio(message):
    pass


@bot.message_handler(content_types=['voice'])
def repeat(message: telebot.types.Message):
    bot.send_message(message.chat.id, 'Да что ты говоришь!')


bot.polling(none_stop=True)
