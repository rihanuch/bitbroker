# Generated by Django 3.0.6 on 2020-07-03 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='telegram_user',
            field=models.CharField(blank=True, max_length=50, verbose_name='telegram user'),
        ),
    ]
