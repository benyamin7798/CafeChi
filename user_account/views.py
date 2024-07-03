from django import forms

from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm,CustomAuthenticationForm
from django.contrib.auth.models import User

def custom_login_view(request):
    if request.method == 'POST':
        identifier = request.POST.get('username')
        password = request.POST.get('password')

        # First try to authenticate with username
        user = authenticate(request, username=identifier, password=password)
        
        if user is None:
            # If authentication with username failed, try email
            try:
                user = User.objects.get(email=identifier)
                username = user.username
                user = authenticate(request, username=username, password=password)
            except User.DoesNotExist:
                pass

        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            # Handle the error case
            context = {'error': 'Invalid credentials'}
            return render(request, 'registration/login.html', context)

    return render(request, 'registration/login.html')


def sign_up_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    
    return render(request, 'registration/sign_up.html', {'form': form})

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
