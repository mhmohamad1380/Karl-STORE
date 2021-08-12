from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input100', 'placeholder': 'Please enter Your Username'}),
        required=True, label='Username')
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input100', 'placeholder': 'Please enter Your Password'}),
        required=True, label='Password')


class RegisterForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input100', 'placeholder': 'Please enter Your Username'}),
        required=True, label='Username')
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'input100', 'placeholder': 'Please enter Your Email'}),
        required=True, label='Email')
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input100', 'placeholder': 'Please enter Your Password '}),
        required=True, label='Password')
    re_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input100', 'placeholder': 'Please enter Your Password Again'}),
        required=True, label='Retype Password')

    def clean_re_password(self):
        password = self.cleaned_data['password']
        re_password = self.cleaned_data['re_password']
        if len(password) < 8 or len(re_password) < 8:
            raise ValidationError('Password Must be 8 Characters or More')
        if password != re_password:
            raise ValidationError('Password and Retype Password should be same')
        return password, re_password

    def clean_username(self):
        username = self.cleaned_data['username']
        is_exist = User.objects.filter(username__iexact=username).exists()
        if is_exist:
            raise ValidationError('this Username is not Available')
        return username
    def clean_email(self):
        email = self.cleaned_data['email']
        is_exist = User.objects.filter(email__iexact=email).exists()
        if is_exist:
            raise ValidationError('this Email is not Available')
        return email
