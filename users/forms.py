from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import Users


class UserLoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField()

    class Meta:
        model = Users
        fields = ("username", "password")
