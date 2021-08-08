# Generated by Django 3.1.5 on 2021-04-21 08:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_bid_category_comments_listing'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='listing',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 21, 10, 46, 30, 467998)),
        ),
    ]
