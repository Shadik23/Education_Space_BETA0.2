from typing import Any, Dict
from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput())
    confirm_password = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput())

    def clean(self):
        all_cleaner_data = super().clean()
        pswd = all_cleaner_data["password"]
        conf = all_cleaner_data["confirm_password"]

        if pswd != conf:
            raise forms.ValidationError('Invalid password')
    
    class Meta():
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

