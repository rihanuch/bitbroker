from django.conf import settings
from bot.telegrambot import BitBrokerBot

urlpatterns = []

BitBrokerBot(settings.BOT_TOKEN)
