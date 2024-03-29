# Generated by Django 2.2.3 on 2019-07-02 09:27

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_auto_20190702_0858'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='issue_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 2, 9, 27, 5, 499264)),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='order_id',
            field=models.UUIDField(default=uuid.UUID('719f5310-6735-47d4-85f2-2e37cbb69a4f'), unique=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('c8bd8d97-4db2-403d-94f3-0685aa142837'), unique=True),
        ),
    ]
