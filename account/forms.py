from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from polls_new.models import TouristPlace


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class CarForm(forms.ModelForm):
    class Meta:
        model = TouristPlace
        fields = ('name', 'description', 'price')