from django import forms

from birds.models import Watch, Bird, Country


class WatchModelForm(forms.ModelForm):
    bird = forms.ModelChoiceField(queryset=Bird.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control'
    }))
    longitude = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    latitude = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    country = forms.ModelChoiceField(queryset=Country.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control'
    }))
    # watched_at =
    description = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control'
    }))
    # author =
    # is_private

    class Meta:
        model = Watch
        fields = ('bird', 'longitude', 'latitude', 'country', 'watched_at', 'description', 'author', 'is_private')
