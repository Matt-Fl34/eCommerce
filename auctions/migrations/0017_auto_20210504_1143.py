# Generated by Django 3.1.5 on 2021-05-04 09:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0016_auto_20210503_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 4, 11, 43, 39, 45036)),
        ),
        migrations.AlterField(
            model_name='listing',
            name='bid',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='listing',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 4, 11, 43, 39, 45036)),
        ),
    ]