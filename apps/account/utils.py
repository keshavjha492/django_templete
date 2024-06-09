import string
from apps.account.models import UserAccountACtivation
from django.conf import settings
import random


def generate_activation_key(user, size=20):
    key = string.ascii_letters + string.digits
    final_key = ""
    for _ in range(size):
        final_key += random.choice(key)
    UserAccountACtivation.objects.create(email=user.email, key=final_key)
    return final_key
        
        
        

def send_email_activation(user, request):
    """
    User: User object
    request: wsgi request object from views
    """

    key = generate_activation_key(user)
    final_url = f"http://127.0.0.1:8000/{user.username}/{key}"
    
    subject ="User Account Activation"
    message = f"""
    please activate your account by clicking on the link below{final_url}"""
    user.email_user(subject=subject, message=message, from_email="settings.FROM_EMAIL")