from django.contrib.auth import get_user_model
import logging
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

User = get_user_model()
from market.model.market import Market
from market.model.currency import Currency


class BitBrokerBot:

    def __init__(self, token):
        self.updater = Updater(token=token, use_context=True)
        self.dispatcher = self.updater.dispatcher

        self.define_commands()
        self.updater.start_polling()

    def define_commands(self):
        start_handler = CommandHandler('start', self.start)
        self.dispatcher.add_handler(start_handler)

        markets_handler = CommandHandler('markets', self.markets)
        self.dispatcher.add_handler(markets_handler)

        currencies_handler = CommandHandler('currencies', self.currencies)
        self.dispatcher.add_handler(currencies_handler)

        echo_handler = MessageHandler(Filters.text & (~Filters.command), self.echo)
        self.dispatcher.add_handler(echo_handler)

    # commands are what follows
    def start(self, update, context):
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="I'm a bot, please talk to me!"
        )

    def markets(self, update, context):
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='\n'.join([str(x) for x in Market.objects.all()])
        )

    def currencies(self, update, context):
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='\n'.join([str(x) for x in Currency.objects.all()])
        )

    def echo(self, update, context):
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=update.message.text
        )


def markets(positions, context):
    pass
