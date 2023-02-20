from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django import forms
from django.utils.safestring import mark_safe


class RegistrationForm(UserCreationForm):
    username = forms.CharField(
        help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        })
    )
    email = forms.CharField(required=True, widget=forms.TextInput(attrs={
            'class': 'form-control'
    }))
    first_name = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    last_name = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    password1 = forms.CharField(
        help_text=mark_safe(
            '''
            <ul>
            <li>Your password can’t be too similar to your other personal information.
            <li>Your password must contain at least 8 characters.
            <li>Your password can’t be a commonly used password.
            <li>Your password can’t be entirely numeric.
            </ul>
            '''),
        widget=forms.PasswordInput(attrs={
            'class': 'form-control'
        })
    )
    password2 = forms.CharField(
        help_text='Enter the same password as before, for verification.',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control'
        })
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control'
        })
    )

    class Meta:
        model = User
        fields = ('username', 'password')


class UserModelForm(forms.ModelForm):
    username = forms.CharField(
        help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        })
    )
    email = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    first_name = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    last_name = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
