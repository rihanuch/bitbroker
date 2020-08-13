from django.core.management.base import BaseCommand
from django.conf import settings
from bot.telegrambot import BitBrokerBot


class Command(BaseCommand):
    help = ''

    def handle(self, *args, **options):
        BitBrokerBot(settings.BOT_TOKEN)
        return self.stdout.write(self.style.SUCCESS('Successfully initialized bot'))
