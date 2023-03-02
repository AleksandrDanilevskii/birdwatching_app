from django import forms
from django.contrib.auth.models import User

from birds.models import Watch, Bird, Country


class WatchModelForm(forms.ModelForm):
    bird = forms.ModelChoiceField(queryset=Bird.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control'
    }))
    longitude = forms.CharField(initial=0.0, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    latitude = forms.CharField(initial=0.0, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    country = forms.ModelChoiceField(queryset=Country.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control'
    }))
    watched_at = forms.DateTimeField(widget=forms.SelectDateWidget(attrs={
        'class': 'form-control'
    }))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={
        'class': 'form-control'
    }))
    author = forms.ModelChoiceField(
        queryset=User.objects.filter(username='adanilevsky'),
        initial=User.objects.filter(username='adanilevsky'),
        # widget=forms.HiddenInput()
    )
    is_private = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
        'class': 'form-check-input'
    }))

    class Meta:
        model = Watch
        fields = ('bird', 'longitude', 'latitude', 'country', 'watched_at', 'description', 'author', 'is_private')
