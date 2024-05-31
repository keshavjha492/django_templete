from django import forms
from django.contrib.auth.forms import get_user_model

User = get_user_model()

class UserRegisterForm(forms.ModelForm):
    class meta:
        model = User
        fields = ["email","first_name","middle_name","last_name"]