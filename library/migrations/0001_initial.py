# Generated by Django 2.2.3 on 2019-07-02 07:17

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('author', models.CharField(max_length=500)),
                ('publisher', models.CharField(max_length=500)),
                ('edition', models.CharField(blank=True, max_length=500, null=True)),
                ('language', models.CharField(max_length=500)),
                ('isbn', models.UUIDField(default=uuid.UUID('9e989f68-2f98-4a8c-8d4c-4efd58190835'), unique=True)),
                ('year', models.IntegerField()),
                ('pages', models.IntegerField()),
                ('abstract', models.CharField(max_length=1000)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='book_photos')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.UUID('1b00d383-c07f-4a05-b69e-a7090f0d513a'), unique=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='profile_pic')),
                ('fine', models.IntegerField(default=0)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.UUIDField(default=uuid.UUID('f763da19-5ec1-4d5e-805e-175645f397ba'), unique=True)),
                ('issue_date', models.DateTimeField(default=datetime.datetime(2019, 7, 2, 7, 17, 21, 163650))),
                ('return_date', models.DateTimeField(blank=True, null=True)),
                ('fine', models.IntegerField(default=0)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.Book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.UserProfile')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='library.Category'),
        ),
    ]
