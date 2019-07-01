from datetime import datetime

from django.db import models

# Create your models here.
from django.contrib.auth.models import User
import uuid


class UserProfile(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4(), unique=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    phone = models.IntegerField()
    address = models.TextField()
    profile_pic = models.ImageField(upload_to='profile_pic', blank=True, null=True)
    fine = models.IntegerField(default=0)


    def __str__(self):
        string = "{} {}".format(self.first_name,self.last_name)
        return string


class Category(models.Model):
    name = models.CharField(max_length=500, blank=False, null=False)
    description = models.CharField(max_length=500, blank=False, null=False)

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

    def __str__(self):
        return self.name


class Inventory(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    order_id = models.UUIDField(default=uuid.uuid4(), unique=True)
    issue_date = models.DateTimeField(default=datetime.now())
    return_date = models.DateTimeField(blank=True, null=True)
    fine = models.IntegerField(default=0)

    def __str__(self):
        return self.order_id