import telebot

TELEGRAM_BOT_API = '5133017011:AAETHW5CWp0GXDNWBp_0GsKj9tDjMXX51Hk'


class GetBot:

    # initial telegram bot
    @staticmethod
    def init_bot():
        bot = telebot.TeleBot(TELEGRAM_BOT_API)
        return bot
