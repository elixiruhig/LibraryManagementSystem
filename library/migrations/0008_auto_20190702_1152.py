# Generated by Django 2.2.3 on 2019-07-02 11:52

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_auto_20190702_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='issue_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 2, 11, 52, 1, 774003)),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='order_id',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
    ]