# Generated by Django 3.1.5 on 2021-04-30 11:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_auto_20210430_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 30, 13, 9, 37, 195469)),
        ),
        migrations.AlterField(
            model_name='listing',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 30, 13, 9, 37, 195469)),
        ),
    ]
