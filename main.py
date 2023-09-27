import telebot

bot = telebot.TeleBot('6468286643:AAEI1F2BPVB1hCU13uPrS0S3QKiz6QYQIcc')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f"Саламчик, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>"
    bot.send_message(message.chat.id, mess, )


@bot.message_handler()
def get_user_text(message):
    if message.text == 'Салам':
        bot.send_message(message.chat.id, "Сагада салам !", )
    elif message.text == 'id':
        bot.send_message(message.chat.id, f"Сенин IDин: {message.from_user.id}", )
    elif message.text == '01':
        audio = open('Where you are halal beats.mp3', 'rb')
        bot.send_audio(message.chat.id, audio)
    elif message.text == '02':
        audio = open('Суйом деп айта албадым.mp3', 'rb')
        bot.send_audio(message.chat.id, audio)
    elif message.text == '03':
        audio = open('Каспийский груз.mp3', 'rb')
        bot.send_audio(message.chat.id, audio)
    elif message.text == '04':
        audio = open('Taweel al shavk halal beats.mp3', 'rb')
        bot.send_audio(message.chat.id, audio)
    elif message.text == '05':
        audio = open('kurtlar vadisi.mp3', 'rb')
        bot.send_audio(message.chat.id, audio)
    elif message.text == '06':
        audio = open('kandine iyi bak.mp3', 'rb')
        bot.send_audio(message.chat.id, audio)
    elif message.text == '07':
        audio = open('Omuzumda ağlayan bir sen.mp3', 'rb')
        bot.send_audio(message.chat.id, audio)
    elif message.text == '08':
        audio = open('Шаштары Урбиіп.mp3', 'rb')
        bot.send_audio(message.chat.id, audio)
    elif message.text == '09':
        audio = open('Baby stop.mp3', 'rb')
        bot.send_audio(message.chat.id, audio)
    elif message.text == 'Фото_01':
        photo = open('1680870331_root-info-p-mers-banana-vkontakte-1.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == 'Фото_02':
        photo = open('photo_2023-09-23_00-45-59.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == 'Фото_03':
        photo = open('photo_2023-09-23_00-46-10.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == 'Фото_04':
        photo = open('photo_2023-09-23_00-46-28.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == 'Видео':
        video = open('378518952_271434289104119_5260462566321070118_n.mp4', 'rb')
        bot.send_video_note(message.chat.id, video)
    else:
        bot.send_message(message.chat.id, "Мен сени тушуно албай жатам!", )


bot.polling(none_stop=True)
