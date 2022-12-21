from django.core.mail import send_mail
import random
from django.conf import settings
from .models import Email_verification
import requests

def send_otp_via_email(email):
    subject = 'Your account verification email'
    otp = random.randint(1000 , 9999)
    message = f'Your otp is {otp}'
    email_from = settings.EMAIL_HOST
    send_mail(subject,message,email_from,[email])
    user_obj = Email_verification.objects.get(email = email)
    user_obj.otp = otp
    user_obj.save()

def send_otp_to_phone(phone):
    try:
        otp = random.randint(1000,9999)
        url = f'https://2factor.in/API/V1/{settings.API_KEY}/SMS/{phone}/{otp}'
        response = requests.get(url)
        return otp
    except Exception as e:
        return e

def send_otp_to_aadharno(aadhar_no):
    try:
        otp = random.randint(1000,9999)
        url = ''
        response = requests.get(url)
        return otp
    except Exception as e:
        return e