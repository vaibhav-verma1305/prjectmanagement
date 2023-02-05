import email
from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.contrib import messages
from .models import Team
from datetime import datetime
import uuid
from gupms.helpers import send_forget_password_mail
from django.db.models import Max
# Create your views here.

def home(request):
    return render(request,"index.html")

def signup(request):
    if request.method == "POST":
        #username = request.POST.get('username')
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        if User.objects.filter(email=email):
            messages.error(request, "Email already exist, Please try some other Email")
            return redirect('/signup')
        if pass1!=pass2:
            messages.error(request,"Password Isn't Match")
            return redirect('/signup')
        myuser= User.objects.create_user(username,email,pass1)
        myuser.save()
        messages.success(request, "Your Account has been Successfully Created."+ username)
        return redirect('/signin')
    return render(request, "signup.html")
def signin(request):
    if request.method =="POST":
        username=request.POST['username']
        password=request.POST['password']
        user= authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/mainpage')
        else:
            pass
    return render(request,"signin.html")
def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully")
    return redirect('home')
def mainpage(request):
    return render(request, "mainpage.html")
def select(request):
    return render(request, "select.html")
def maketeam(request):
    regno = 1000  if Team.objects.count() == 0 else  Team.objects.aggregate(max=Max('regnumber'))["max"]+1
    if request.method == "POST":
        enrollment1=request.POST.get('enrollment1')
        admission1=request.POST.get('admission1')
        name1 = request.POST.get('name1')
        email1 = request.POST.get('email1')
        phone1 = request.POST.get('phone1') 
        enrollment2=request.POST.get('enrollment2')
        admission2=request.POST.get('admission2')
        name2 = request.POST.get('name2')
        email2 = request.POST.get('email2')
        phone2 = request.POST.get('phone2')
        enrollment3=request.POST.get('enrollment3')
        admission3=request.POST.get('admission3')
        name3 = request.POST.get('name3')
        email3 = request.POST.get('email3')
        phone3 = request.POST.get('phone3')       
            
        maketeam =Team(regnumber=regno,enrollment1=enrollment1,admission1=admission1,name1=name1, email1=email1, phone1=phone1,enrollment2=enrollment2,admission2=admission2,name2=name2, email2=email2, phone2=phone2,enrollment3=enrollment3,admission3=admission3,name3=name3, email3=email3, phone3=phone3)
        maketeam.save()
        return redirect('mainpage')
    return render(request, "maketeam.html")
def teamdetails(request):
    details = Team.objects.all()
    return render(request,"teamdetails.html", {'details' : details })
def signout(request):
    logout(request)
    return redirect('home')
def send(request, token):
    token = str(uuid.uuid4())
    send_mail('Your Forget Password Link',
    'Hi, Click On the link to reset your Password http://127.0.0.1:8000/change_password/{token}/',
    'mrbajaj422@gmail.com',
    [email],
    fail_silently=False)
    return render(request,"send.html")
def password_reset_complete(request):
    return render(request,"password_reset_complete")
def password_reset_confirm(request):
    return render(request,"password_reset_confirm")
def password_reset_done(request):
    return render(request,"password_reset_done")
def password_reset_email(request):
    return render(request,"password_reset_email")
def password_reset_form(request):
    return render(request,"password_reset_form")
def sample(request):
    return render(request,"sample.html")
def contact(request):
    return render(request,"contact.html")

