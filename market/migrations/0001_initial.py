# Generated by Django 3.0.8 on 2020-07-04 02:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_cryptography.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('symbol', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('action', models.CharField(choices=[('BUY', 'Buy'), ('SELL', 'Sell')], default='BUY', max_length=4)),
                ('from_amount', models.FloatField()),
                ('to_amount', models.FloatField()),
                ('from_currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions_from', to='market.Currency')),
                ('market', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.Market')),
                ('to_currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions_to', to='market.Currency')),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desired_return', models.FloatField()),
                ('market', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='positions', to='market.Market')),
                ('transaction_buy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='positions_buy', to='market.Transaction')),
                ('transaction_sell', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='positions_sell', to='market.Transaction')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='positions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Key',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_key', django_cryptography.fields.encrypt(models.CharField(blank=True, max_length=500, null=True))),
                ('api_secret', django_cryptography.fields.encrypt(models.CharField(blank=True, max_length=500, null=True))),
                ('market', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='keys', to='market.Market')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='keys', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
