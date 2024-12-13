from django import forms
from django.contrib.admin.forms import AuthenticationForm
class login(AuthenticationForm):
    user_name=forms.CharField(max_length=30,label="имя пользователя",
                              widget=forms.TextInput({'placeholder':'Имя пользователя'}))
    password=forms.CharField(min_length=8,max_length=30,label='Пароль',widget=forms.PasswordInput({'placeholder':'Пароль'}))
    pass