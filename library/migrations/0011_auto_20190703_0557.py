# Generated by Django 2.2.3 on 2019-07-03 05:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0010_auto_20190703_0542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='issue_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 3, 5, 57, 8, 609764)),
        ),
    ]
