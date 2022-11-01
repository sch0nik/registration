from django.core.management import BaseCommand
from telegram.ext import Updater, MessageHandler, Filters

from registration import settings
from users.models import RegistrationCode, TelegramID

updater = Updater(token=settings.API_TOKEN)

dispatcher = updater.dispatcher


def response(update, context):
    code = int(update.message.text)
    tg_id = update.effective_chat.id
    code = RegistrationCode.objects.filter(code__exact=code)
    if code:
        user = code[0].user
        if user:
            user.telegram_id.telegram_id = tg_id
            user.telegram_id.save()
        else:
            telegram_id = TelegramID(telegram_id=tg_id, user=user)
            telegram_id.save()

        text = 'The code is correct. Are you registered.'
    else:
        text = 'Invalid code, please try again'
    context.bot.send_message(chat_id=tg_id, text=text)


resp_handler = MessageHandler(Filters.text & (~Filters.command), response)
dispatcher.add_handler(resp_handler)


class Command(BaseCommand):
    help = 'Run bot'

    def handle(self, *args, **options):
        updater.start_polling()
