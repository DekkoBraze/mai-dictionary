from django import forms


class TranslationForm(forms.Form):
    word1 = forms.CharField(max_length=255, label='Русский')
    word2 = forms.CharField(max_length=255, label='Английский')
