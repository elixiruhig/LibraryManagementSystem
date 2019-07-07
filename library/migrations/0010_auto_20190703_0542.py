# Generated by Django 2.2.3 on 2019-07-03 05:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0009_auto_20190703_0531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='issue_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 3, 5, 42, 0, 151356)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(default='default.png', upload_to='profile_pic'),
        ),
    ]
