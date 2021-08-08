# Generated by Django 3.1.5 on 2021-04-24 11:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_auto_20210423_0954'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 24, 13, 38, 13, 803339)),
        ),
        migrations.AlterField(
            model_name='listing',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 24, 13, 38, 13, 803339)),
        ),
        migrations.AlterField(
            model_name='listing',
            name='image',
            field=models.URLField(),
        ),
    ]
