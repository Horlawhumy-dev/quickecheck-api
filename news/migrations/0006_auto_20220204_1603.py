# Generated by Django 3.2 on 2022-02-04 15:03

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20220204_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hackernewsid',
            name='fetched_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 4, 16, 3, 45, 389489)),
        ),
        migrations.AlterField(
            model_name='quickcheckitem',
            name='id',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='news.hackernewsid'),
        ),
    ]
