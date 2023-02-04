from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views  

urlpatterns = [
   path('', views.home, name="home"),
   path('signup', views.signup, name="signup"),
   path('signin', views.signin, name="signin"),
   path('signout', views.signout, name="signout"),
   path('mainpage', views.mainpage, name="mainpage"),
   path('select', views.select, name="select"),
   path('first_year', views.first_year, name="first_year"),
   path('second_year', views.second_year, name="second_year"),
   path('third_year', views.third_year, name="third_year"),
   path('fourth_year', views.fourth_year, name="fourth_year"),
   path('send/', views.send, name="send"),
   path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
   path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
   path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
   path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
   path('contact', views.contact, name="contact"),
   path('signup_student_page', views.signup_student_page, name="signup_student_page"),
   path('signup_admin_page', views.signup_admin_page, name="signup_admin_page"),
   path('signup_staff_page', views.signup_staff_page, name="signup_staff_page"),
   path('student_dashboard', views.student_dashboard, name="student_dashboard"),
   path('staff_dashboard', views.staff_dashboard, name="staff_dashboard"),
   path('admin_dashboard', views.admin_dashboard, name="admin_dashboard"),
]