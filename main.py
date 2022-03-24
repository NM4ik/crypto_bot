import telebot
import botApi

bot = botApi.GetBot.init_bot()


@bot.message_handler(commands=['start', 'старт'])
def start(message):
    value = f'Привет, <b>{message.from_user.first_name}</b>'
    bot.send_message(message.chat.id, value, parse_mode='html')


# works all time
bot.polling(none_stop=True)
