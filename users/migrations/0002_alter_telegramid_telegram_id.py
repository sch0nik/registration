# Generated by Django 4.1.3 on 2022-11-01 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telegramid',
            name='telegram_id',
            field=models.CharField(max_length=100, verbose_name='Telegram id'),
        ),
    ]