import random
from datetime import datetime

from django.views.generic import TemplateView

from registration import settings
from users.models import RegistrationCode


class IndexView(TemplateView):
    template_name = 'base.html'


class BotUrlView(TemplateView):
    template_name = 'bot.html'

    def get_context_data(self, **kwargs):
        context = super(BotUrlView, self).get_context_data()
        context['bot_name'] = settings.TELEGRAM_BOT_NAME
        if self.request.GET.get('generate') == 'yes':
            code = random.randint(10_000, 100_000)
            context['reg_code'] = code
            user = self.request.user
            if user.reg_code:
                user.reg_code.code = code
                user.reg_code.created_at = datetime.now()
                user.reg_code.save()
            else:
                code = RegistrationCode(code=code)
                user.reg_code = code
                code.save()
        return context
