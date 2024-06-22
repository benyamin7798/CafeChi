from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30,required=True,help_text='your name...')
    last_name = forms.CharField(max_length=30, required=True,help_text='last name ...')
    email = forms.EmailField(max_length=254,required=True,help_text='Enter your Email ...')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        