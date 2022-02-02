# Generated by Django 3.2 on 2022-02-02 13:10

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20220202_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news_id',
            name='fetched_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 2, 14, 10, 53, 607006)),
        ),
        migrations.AlterField(
            model_name='newsitem',
            name='id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='news.news_id'),
        ),
    ]