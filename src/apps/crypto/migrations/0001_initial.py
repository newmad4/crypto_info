# Generated by Django 4.0.2 on 2022-02-04 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExchangeRateHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('exchange_rate', models.DecimalField(decimal_places=8, max_digits=18)),
                ('from_currency', models.CharField(max_length=10)),
                ('to_currency', models.CharField(max_length=10)),
            ],
        ),
    ]
