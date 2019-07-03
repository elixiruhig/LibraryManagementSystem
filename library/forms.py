
from django import forms
from django.contrib.auth.models import User
from django.forms import PasswordInput

from library.models import UserProfile, Book


class UserForm(forms.ModelForm):

    password = forms.CharField(widget=PasswordInput)

    class Meta():
        model = User
        fields = ('username','password','email')

    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = ''
        self.fields['password'].help_text = ''
        self.fields['email'].help_text = ''

class UserProfileForm(forms.ModelForm):

    class Meta():
        model = UserProfile
        fields = ('first_name','last_name','phone','address','profile_pic')

    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].help_text = ''
        self.fields['last_name'].help_text = ''
        self.fields['phone'].help_text = ''
        self.fields['address'].help_text = ''
        self.fields['profile_pic'].help_text = ''

class BookForm(forms.ModelForm):

    class Meta():
        model = Book
        fields = '__all__'