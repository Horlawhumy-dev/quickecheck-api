# Generated by Django 3.2 on 2022-02-04 14:43

import datetime
import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_alter_hackernewsid_fetched_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hackernewsid',
            name='fetched_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 4, 15, 43, 57, 726179)),
        ),
        migrations.AlterField(
            model_name='quickcheckitem',
            name='kids',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.BigIntegerField(blank=True, null=True, unique=True), size=None), size=None),
        ),
    ]
