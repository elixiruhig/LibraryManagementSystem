from datetime import datetime

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from library.forms import UserForm, UserProfileForm
from library.models import Book, Inventory, UserProfile


def homeview(request):
    if request.method == 'POST':
        user = UserProfile.objects.get(user = request.user)
        book = Book.objects.get(isbn=request.POST['borrow'])
        if book.quantity == 0:
            return HttpResponse('Book out of stock')
        book.quantity -= 1
        book.save()
        inventory = Inventory()
        inventory.book = book
        inventory.user = user
        inventory.save()
    books = Book.objects.all()
    context = {'books':books}
    return render(request,'library/home.html',context)

def signout(request):
    logout(request)
    return render(request, 'library/home.html')

def user_login(request):
    if request.method == 'POST':
        if 'login' in request.POST:
            username = request.POST['uname']
            password = request.POST['pass']
            user = authenticate(username = username,password = password)
            if user:
                if user.is_active:
                    login(request,user)
                    return redirect('library:homeview')
                else:
                    return HttpResponse('Account inactive')
            else:
                print("Failed login at username: {} and password: {}".format(username,password))
                return HttpResponse('Invalid login')

    else:
        return render(request, 'library/login.html')

def register(request):
    if request.method == 'POST':
        user_form = UserForm(data = request.POST)
        profile_form = UserProfileForm(request.POST,request.FILES)
        print("UserForm.errors: {} \n ProfileForm.errors: {}".format(user_form.errors,profile_form.errors))
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)

            profile.user = request.user.id
            profile.save()
            return render(request,'library/login.html',{'message':'Login to your account'})
        else:
            return HttpResponse('{} {}'.format(user_form.errors,profile_form.errors))

    elif request.method == 'GET':
        user_form = UserForm()
        profile_form = UserProfileForm()
        return render(request,'library/register.html',{'user_form':user_form,'profile_form':profile_form})

def user_profile(request,profile):
    if request.method == 'POST':
        id = request.POST['return']
        inv = Inventory.objects.get(order_id=id)
        book = Book.objects.get(id = inv.book.id)
        book.quantity += 1
        book.save()
        inv.return_date = datetime.now()
        days = inv.return_date - inv.issue_date
        fine = 0
        if days.days> 30:
            if days.days < 35:
                for i in range(days.days - 30):
                    fine += 5
            else:
                for i in range(days.days - 30):
                    fine += 5
                for i in range(35,days.days):
                    fine += 10
        inv.fine = fine
        inv.status = True
        inv.save()



    user = UserProfile.objects.get(user = User.objects.get(username=profile))
    inventorys = Inventory.objects.filter(user = user)
    return render(request,'library/user_profile.html',{'user':user,'inventorys':inventorys})