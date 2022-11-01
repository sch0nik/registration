from django.contrib.auth.models import User
from django.db import models


class TelegramID(models.Model):
    telegram_id = models.CharField('Telegram id', max_length=100, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='telegram_id')


class RegistrationCode(models.Model):
    code = models.IntegerField()
    created_at = models.DateTimeField('Created at', auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='reg_code')
