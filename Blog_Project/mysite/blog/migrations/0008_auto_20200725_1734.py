# Generated by Django 3.0.3 on 2020-07-25 12:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200725_1726'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='created_date',
        ),
        migrations.AddField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 25, 12, 4, 40, 704875, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 25, 12, 4, 40, 704875, tzinfo=utc)),
        ),
    ]
