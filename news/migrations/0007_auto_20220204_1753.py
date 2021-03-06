# Generated by Django 3.2 on 2022-02-04 16:53

import datetime
import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20220204_1603'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuickCheckNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('by', models.CharField(max_length=255)),
                ('kids', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.BigIntegerField(blank=True, null=True, unique=True), size=None), size=None)),
                ('parent', models.IntegerField(blank=True, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('title', models.CharField(max_length=255)),
                ('score', models.IntegerField(blank=True, null=True)),
                ('descendants', models.IntegerField(blank=True, null=True)),
                ('deleted', models.BooleanField(default=False)),
                ('time', models.BigIntegerField(blank=True, default=1643993618.133793, null=True, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='hackernewsid',
            name='fetched_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 4, 17, 53, 38, 132794)),
        ),
        migrations.AlterField(
            model_name='quickcheckitem',
            name='time',
            field=models.BigIntegerField(blank=True, default=1643993618.133793, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='quickcheckitem',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
