# Generated by Django 3.2 on 2022-02-07 12:07

import datetime
import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0012_auto_20220206_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hackernewsid',
            name='fetched_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 7, 13, 7, 12, 805615)),
        ),
        migrations.AlterField(
            model_name='quickcheckitem',
            name='time',
            field=models.BigIntegerField(blank=True, default=1644235633, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='quickchecknews',
            name='kids',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.BigIntegerField(blank=True, null=True), size=None), size=None),
        ),
        migrations.AlterField(
            model_name='quickchecknews',
            name='time',
            field=models.BigIntegerField(blank=True, default=1644235633, null=True, unique=True),
        ),
    ]
