# Generated by Django 3.2 on 2022-02-02 13:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_alter_news_id_fetched_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news_id',
            name='fetched_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 2, 14, 16, 45, 475369)),
        ),
        migrations.AlterField(
            model_name='newsitem',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
