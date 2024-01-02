import telebot


bot = telebot.TeleBot('6574029714:AAEQqewHpbwouJwTdz-qAxLzKb217JbBhDI')

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    bot.send_message(user_id, 'Hello everyone!')


@bot.message_handler(commands=['help'])
def help_command(message):
    user_id = message.from_user.id
    bot.send_message(user_id, 'Commands\n'
                     '/start for start bot\n'
                     '/help to show all commands\n'
                     '/help_me to contact us')


@bot.message_handler(commands=['help_me'])
def help_me(message):
    user_id = message.from_user.id
    bot.send_message(user_id, 'Admin: @AADEMAN\n'
                     'Phon number: +9989100XXXXX\n'
                     'E-mail: dxxxxxxxxx@gmail.com')


bot.polling(non_stop=True)