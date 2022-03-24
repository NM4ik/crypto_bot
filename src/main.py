import datetime

import botApi
from telebot import types
from src.getPrice import GetPrice

bot = botApi.GetBot.init_bot()

import datetime


# init message
@bot.message_handler(commands="start")
def cmd_start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btc_button = types.InlineKeyboardButton(text="BTC/USDT", callback_data='1')
    eth_button = types.InlineKeyboardButton(text="ETH/USDT", callback_data='2')

    keyboard.add(btc_button, eth_button)
    bot.send_message(message.chat.id, 'Select the desired cryptocurrency', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text != 0:
        crypto = message.text[:3:1]
        print(crypto+'USDT')
        data = GetPrice.get_price(crypto+'USDT')

        result = formatter(data, message.text)
        bot.send_message(message.chat.id, result, parse_mode='html')
    else:
        bot.send_message(message.chat.id, 'IT IS ETH')


def formatter(data, text):
    return f'<b>{text}</b>\nPrice for sale: <b>{data["askPrice"]}</b>\nPurchase price: <b>{data["bidPrice"]}</b>'


# works all time
bot.polling(none_stop=True)
