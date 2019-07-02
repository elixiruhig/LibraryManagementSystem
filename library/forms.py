
from django import forms
from django.contrib.auth.models import User
from django.forms import PasswordInput

from library.models import UserProfile, Book


class UserForm(forms.ModelForm):

    password = forms.CharField(widget=PasswordInput)

    class Meta():
        model = User
        fields = ('username','password','email')

class UserProfileForm(forms.ModelForm):

    class Meta():
        model = UserProfile
        fields = ('first_name','last_name','phone','address','profile_pic')

class BookForm(forms.ModelForm):

    class Meta():
        model = Book
        fields = '__all__'