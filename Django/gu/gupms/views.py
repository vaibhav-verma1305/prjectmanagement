import email
from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.contrib import messages
from .models import First_year
from .models import Second_year
from .models import Third_year
from .models import Fourth_year
from .models import Profile
from .models import *
from datetime import datetime
import uuid
from django.db.models import Max
from django.shortcuts import render, redirect
from .forms import StudentSignupForm, StaffSignupForm, AdminSignupForm
from .models import User
from django.views.decorators.csrf import csrf_protect
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
@csrf_protect
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_student:
                return redirect('student_dashboard')
            elif user.is_staff:
                return redirect('staff_dashboard')
            elif user.is_admin:
                return redirect('admin_dashboard')
        else:
            return render(request, 'signin.html', {'error_message': 'Invalid login credentials'})
    return render(request, 'signin.html')
def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully")
    return redirect('home')
def mainpage(request):
    return render(request, "mainpage.html")
def select(request):
    return render(request, "select.html")
def first_year(request):
    regno = 1000  if First_year.objects.count() == 0 else  First_year.objects.aggregate(max=Max('regnumber'))["max"]+1
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
            
        first_year =First_year(regnumber=regno,enrollment1=enrollment1,admission1=admission1,name1=name1, email1=email1, phone1=phone1,enrollment2=enrollment2,admission2=admission2,name2=name2, email2=email2, phone2=phone2,enrollment3=enrollment3,admission3=admission3,name3=name3, email3=email3, phone3=phone3)
        first_year.save()
        return redirect('mainpage')
    return render(request, "first_year.html")
def second_year(request):
    regno = 1000  if Second_year.objects.count() == 0 else  Second_year.objects.aggregate(max=Max('regnumber'))["max"]+1
    if request.method == "POST":

        enrollment4=request.POST.get('enrollment4')
        admission4=request.POST.get('admission4')
        name4 = request.POST.get('name4')
        email4 = request.POST.get('email4')
        phone4 = request.POST.get('phone4') 
        enrollment5=request.POST.get('enrollment5')
        admission5=request.POST.get('admission5')
        name5 = request.POST.get('name5')
        email5 = request.POST.get('email5')
        phone5 = request.POST.get('phone5')
        enrollment6=request.POST.get('enrollment6')
        admission6=request.POST.get('admission6')
        name6 = request.POST.get('name6')
        email6 = request.POST.get('email6')
        phone6 = request.POST.get('phone6')       
            
        second_year =Second_year(regnumber=regno,enrollment4=enrollment4,admission4=admission4,name4=name4, email4=email4, phone4=phone4,enrollment5=enrollment5,admission5=admission5,name5=name5, email5=email5, phone5=phone5,enrollment6=enrollment6,admission6=admission6,name6=name6, email6=email6, phone6=phone6)
        second_year.save()
        return redirect('mainpage')
    return render(request, "second_year.html")
def third_year(request):
    regno = 1000  if Third_year.objects.count() == 0 else  Third_year.objects.aggregate(max=Max('regnumber'))["max"]+1
    if request.method == "POST":

        enrollment7=request.POST.get('enrollment7')
        admission7=request.POST.get('admission7')
        name7 = request.POST.get('name7')
        email7 = request.POST.get('email7')
        phone7 = request.POST.get('phone7') 
        enrollment8=request.POST.get('enrollment8')
        admission8=request.POST.get('admission8')
        name8 = request.POST.get('name8')
        email8 = request.POST.get('email8')
        phone8 = request.POST.get('phone8')
        enrollment9=request.POST.get('enrollment9')
        admission9=request.POST.get('admission9')
        name9 = request.POST.get('name9')
        email9 = request.POST.get('email9')
        phone9 = request.POST.get('phone9')       
            
        third_year = Third_year(regnumber=regno,enrollment7=enrollment7,admission7=admission7,name7=name7, email7=email7, phone7=phone7,enrollment8=enrollment8,admission8=admission8,name8=name8, email8=email8, phone8=phone8,enrollment9=enrollment9,admission9=admission9,name9=name9, email9=email9, phone9=phone9)
        third_year.save()
        return redirect('mainpage')
    return render(request, "third_year.html")
def fourth_year(request):
    regno = 1000  if Fourth_year.objects.count() == 0 else  Fourth_year.objects.aggregate(max=Max('regnumber'))["max"]+1
    if request.method == "POST":

        enrollment10=request.POST.get('enrollment10')
        admission10=request.POST.get('admission10')
        name10 = request.POST.get('name10')
        email10 = request.POST.get('email10')  
        phone10 = request.POST.get('phone10') 
        enrollment11=request.POST.get('enrollment11')
        admission11=request.POST.get('admission11')
        name11 = request.POST.get('name11')
        email11 = request.POST.get('email11')
        phone11 = request.POST.get('phone11')
        enrollment12=request.POST.get('enrollment12')
        admission12=request.POST.get('admission12')
        name12 = request.POST.get('name12')
        email12 = request.POST.get('email12')
        phone12= request.POST.get('phone12')       
            
        fourth_year =Fourth_year(regnumber=regno,enrollment10=enrollment10,admission10=admission10,name10=name10, email10=email10, phone10=phone10,enrollment11=enrollment11,admission11=admission11,name11=name11, email11=email11, phone11=phone11,enrollment12=enrollment12,admission12=admission12,name12=name12, email12=email12, phone12=phone12)
        fourth_year.save()
        return redirect('mainpage')
    return render(request, "fourth_year.html")
def signout(request):
    logout(request)
    return redirect('home')
def forgot_password(request):
    try:
        if request.method=='POST':
            username=request.POST.get('username')
            if not User.objects.filter(username=username).first():
                messages.success(request,"Not User Found of this Username")
                return redirect('forgot_password')
            user_obj=User.objects.get(username=username)
            token = str(uuid.uuid4())
            profile_obj= Profile.objects.get(user=user_obj)
            profile_obj.forget_password_token= token
            profile_obj.save()
            send(user_obj, token)
            messages.success(request,"An Email is Sent")
            return redirect('forgot_password')
    except Exception as e:
        print(e)
    return render(request, "forgot_password.html")
def change_password(request, token):
    context={}
    try:
        profile_obj=Profile.objects.filter(forget_password_token= token).first()
        context={'user_id': profile_obj.user.id}
        if request.method=="POST":
            pass1=request.POST.get('pass1')
            pass2=request.POST.get('pass2')
            user_id=request.Post.get('user_id')
            if user_id is None:
                messages.success(request,"NO User Id found.")
                return redirect(f'change_password{token}')
            if pass1 != pass2:
                messages.success(request,"Both Are Equal")
                return redirect(f'change_password{token}')
            user_obj=User.objects.get(id=user_id)
            user_obj.set_password(pass1)
            user_obj.save()
            return redirect('/signin')
        context={'user_id': profile_obj.user.id}
        print(profile_obj)
    except Exception as e:
        print(e)
    return render(request, "change_password.html", context)
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
def contact(request):
    return render(request,"contact.html")
def signup_student_page(request):
    if request.method == 'POST':
        form = StudentSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_student = True
            user.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('/signin')
    else:
        form = StudentSignupForm()
    return render(request, 'signup_student.html', {'form': form})
def signup_admin_page(request):
    if request.method == 'POST':
        form = AdminSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_admin = True
            user.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('/signin')
    else:
        form = AdminSignupForm()
    return render(request, "signup_admin_page.html", {'form': form})
def signup_staff_page(request):
    if request.method == 'POST':
        form = StaffSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = True
            user.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('/signin')
    else:
        form = StaffSignupForm()
    return render(request, "signup_staff_page.html", {'form': form})
def student_dashboard(request):
    return render(request,"student_dashboard.html")
def staff_dashboard(request):
    return render(request,"staff_dashboard.html")
def admin_dashboard(request):
    return render(request,"admin_dashboard.html")
