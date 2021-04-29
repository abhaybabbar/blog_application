from django.utils.text import slugify
import string
import random
from django.conf import settings
from django.core.mail import send_mail

def generate_random_string(N):
    res = ''.join(random.choices(string.ascii_uppercase+string.digits, k=N))
    return res

def generate_slug(text):
    new_slug = slugify(text)
    from .models import BlogModel
    if BlogModel.objects.filter(slug = new_slug).exists():
        new_slug = generate_slug(text + generate_random_string(5))
    return new_slug

def send_mail_to_user(token, email):
    subject = f'Your accout needs to be verified'
    message = f"Hi, paste the link to verify account http://127.0.0.1:8000/verify/{token}"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject=subject, message=message, from_email=email_from,recipient_list=recipient_list)
    print("Email Sent")
    return True