from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')
    
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['email', 'username', 'password1', 'password2']  # Fields to be displayed in the form

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter email'})
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter username'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirm password'})


class SigninForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'}))
    

class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['bio', 'location', 'job', 'profile_picture']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['bio', 'location', 'job', 'profile_picture']
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your bio'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your location'}),
            'job': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your job'}),
        }