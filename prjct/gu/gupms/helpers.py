from django.core.mail import send_mail
import uuid
from django.conf import settings



def send_forget_password_mail(email, token):
    token=str(uuid.uuid4())
    subject= 'Your Forget Password Link'
    message =f'Hi, Click On the link to reset your Password http://127.0.0.1:8000/change_password/{token}/'
    email_from = settings.EMAIL_HOST_USER
    recipient_list=[email]
    send_mail(subject,message,email_from,recipient_list)
    return True