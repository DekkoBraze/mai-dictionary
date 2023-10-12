from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class TranslationForm(forms.Form):
    word1 = forms.CharField(max_length=255, label='Русский')
    word2 = forms.CharField(max_length=255, label='Английский')
