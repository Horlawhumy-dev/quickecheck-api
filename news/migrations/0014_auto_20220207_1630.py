# Generated by Django 3.2 on 2022-02-07 15:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0013_auto_20220207_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hackernewsid',
            name='fetched_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 7, 16, 30, 29, 37324)),
        ),
        migrations.AlterField(
            model_name='quickcheckitem',
            name='time',
            field=models.BigIntegerField(blank=True, default=1644247830, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='quickchecknews',
            name='time',
            field=models.BigIntegerField(blank=True, default=1644247830, null=True, unique=True),
        ),
    ]
