from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30,required=True,help_text='your name...')
    last_name = forms.CharField(max_length=30, required=True,help_text='last name ...')
    email = forms.EmailField(max_length=254,required=True,help_text='Enter your Email ...')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')



class CustomAuthenticationForm(forms.Form):
    username_or_email = forms.CharField(label="Username or Email")
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username_or_email = cleaned_data.get('username_or_email')
        password = cleaned_data.get('password')

        if username_or_email and password:
            user = authenticate(username=username_or_email, password=password)
            if not user:
                # Check if the input is an email
                try:
                    user_obj = User.objects.get(email=username_or_email)
                    user = authenticate(username=user_obj.username, password=password)
                except User.DoesNotExist:
                    raise forms.ValidationError("Invalid login credentials")
            
            #if not user:
                #raise forms.ValidationError("Invalid login credentials")
            self.user = user
        return cleaned_data

    def get_user(self):
        return self.user