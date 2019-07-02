from datetime import datetime

from django.db import models

# Create your models here.
from django.contrib.auth.models import User
import uuid


class UserProfile(models.Model):
    uuid = models.UUIDField(unique=True, default=uuid.uuid4)
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    phone = models.IntegerField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profile_pic', default='media/default.png')
    fine = models.IntegerField(default=0)


    def __str__(self):
        string = "{} {}".format(self.first_name,self.last_name)
        return string


class Category(models.Model):
    name = models.CharField(max_length=500, blank=False, null=False)
    description = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=500, blank=False, null=False)
    author = models.CharField(max_length=500, blank=False, null=False)
    publisher = models.CharField(max_length=500, blank=False, null=False)
    edition = models.CharField(max_length=500, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    language = models.CharField(max_length=500, blank=False, null=False)
    isbn = models.IntegerField()
    year = models.IntegerField()
    pages = models.IntegerField()
    abstract = models.CharField(max_length=1000, blank=False, null=False)
    photo = models.ImageField(upload_to='book_photos',default='media/default.png')
    quantity = models.IntegerField(default=10)

    def __str__(self):
        return self.name


class Inventory(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    order_id = models.UUIDField(unique=True, default=uuid.uuid4)
    issue_date = models.DateTimeField(default=datetime.now())
    return_date = models.DateTimeField(blank=True, null=True)
    fine = models.IntegerField(default=0)
    status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.order_id)