
import json,time,requests
from django.contrib.auth import get_user_model
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from random import randint
from app_event.models import Event
from app_profile.models import Profile
from app_profile.forms import SignUpForm
from app_profile.models import Contact
from django.conf import settings
import datetime


def account(request, username):

    try:
        pro = User.objects.get(username=username)
    except User.DoesNotExist:
        return HttpResponseRedirect(reverse('not_find'))
    event = Event.objects.all()
    return render(request, 'user-profile.html', {'pro': pro, 'event': event})


def coming_soon(request):
  return render(request, 'coming-soon.html')


@login_required
def inbox(request):
    mess = messages.objects.all()
    if request.method == "POST":
        sender = request.user
        resiver = request.POST.get("resiver")
        message = request.POST.get("message")
        inbox = messages()
        inbox.sender = sender
        inbox.resiver = resiver
        inbox.message = message

        inbox.save()
        return render(request, 'dashboard-messages.html', {'mess': mess})
    else:
      return render(request, 'dashboard-messages.html', {'mess': mess})


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        recaptcha_response = request.POST.get('g-recaptcha-response')
        sec = settings.RECAPTCHA_SECRET_KEY
        data = {
           'response': recaptcha_response,
           'secret': sec
        }
        r = requests.post(
            'https://www.google.com/recaptcha/api/siteverify', data=data)
        result = r.json()
        if not User.objects.filter(username=username):

               User.objects.create_user(username=username, password=password)
               user = authenticate(username=username, password=password)
               login(request,user)
               return redirect('dashboard')
        elif not result.get('success'):
           messages.success(request, 'sry recaptcha')
           return redirect('signup')

        else:
           messages.success(
               request, 'نام کاربری وارد شده موجود است لطفا نام کاربری دیگری را امتحان کنید')
           return redirect('signup')

    else:
      return render(request, 'signup.html')


def confrim_number(request):

    if request.method == 'POST':
      number = request.POST.get('number')
      message = randint(10000, 99999)
      request.user.profile.code = message
      request.user.profile.tell = number
      request.user.save()
      print(message)
      url="https://ippanel.com/services.jspd"
      param={
    
          "op" : "send",
            "uname" : "",
            "pass":  "",
            "message" :'سلام به هم تیمی خوش آمدید کد فعال سازی شما:{}'.format(message),
            "from": "",
            "to" :number,

}
      requests.post(url,data=param)
      tt=requests.post(url,data=param)
      print(tt)
      messages.success(request, 'کد فعال سازی ارسال شد')
      return redirect('authenticate')
    else:
      return render(request, 'authenticate.html')


def verify_phone(request):
    t=request.user.profile.code

    print(t)
    if request.method == 'POST':
       sms_code=request.POST.get('sms')

       if int(sms_code) == t:
             print('good')
             return redirect('my-profile')
       else:
          messages.error(request, 'کد وارد شده اشتباه است')
          return redirect('authenticate')

    else:
      return render(request, 'authenticate.html')


def login_costum(request):
    if request.method == 'POST':
      username=request.POST.get('username')
      password=request.POST.get('password')
      user=authenticate(username=username,password=password)
      if user:
             
            login(request,user)
            return redirect('dashboard')
      else:
         messages.error(request,'پسورد یا نام کاربری را اشتباه وارد کردید')
         return redirect('loginn')      
    
          
            

      
    
  
      
    else:
    
       return render(request,'login.html')


def signout(request):
    logout(request)
    return redirect(reverse('home'))


@login_required
def profile(request):
    if request.method == 'POST':
        request.user.profile.avatar=request.FILES.get('avatar')
        request.user.first_name=request.POST.get('first_name')
        request.user.last_name=request.POST.get('last_name')
        request.user.profile.bio=request.POST.get('bio')
        request.user.profile.birth_date=request.POST.get('birth_date')
        request.user.profile.telegram=request.POST.get('telegram')
        request.user.profile.instagram=request.POST.get('instagram')
        request.user.profile.city=request.POST.get('city')
        request.user.profile.gender=request.POST.get('gender')
        request.user.profile.tell=request.POST.get('mobile_number')
        request.user.profile.email=request.POST.get('email')
        request.user.profile.favorite=request.POST.get('favorite')
        request.user.profile.orgin_fav=request.POST.get('org_fav')
        request.user.save()
        form=PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user=form.save()
            update_session_auth_hash(request, user)
            return redirect('home')
    else:
        form=PasswordChangeForm(request.user)
    return render(request, 'dashboard-my-profile.html', {'form': form})




def contact(request):
   if request.method == 'POST':
        name=request.POST.get('name')
        tell=request.POST.get('tell')
        message=request.POST.get('messages')
        email=request.POST.get('email')
        title=request.POST.get('title')
        contact=Contact()
        contact.name=name
        contact.tell=tell
        contact.messages=message
        contact.email=email
        contact.title=title
        contact.save()
        messages.success(request, 'پیام شما ارسال شد')
        return redirect("contact")
   else:

      return render(request, 'contact.html')






# sudo apt install postgresql-10-postgis-2.4 postgresql-10-postgis-2.4-scripts
# https://wiki.userside.eu/%D0%A3%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B0_PostgreSQL
