# Generated by Django 3.2 on 2022-02-04 14:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hackernewsid',
            name='id',
        ),
        migrations.AlterField(
            model_name='hackernewsid',
            name='fetched_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 4, 15, 13, 4, 852302)),
        ),
        migrations.AlterField(
            model_name='hackernewsid',
            name='hackernews',
            field=models.BigIntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]
