# Generated by Django 3.2 on 2022-02-04 14:29

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20220204_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hackernewsid',
            name='fetched_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 4, 15, 29, 45, 184588)),
        ),
        migrations.AlterField(
            model_name='quickcheckitem',
            name='id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='news.hackernewsid'),
        ),
    ]
