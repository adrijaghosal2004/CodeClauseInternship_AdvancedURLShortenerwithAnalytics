from .models import Short
from django import forms

class newShortUrl(forms.ModelForm):
    class Meta:
        model=Short
        fields = ['originalUrl']        
        widgets = {
            'originalUrl': forms.TextInput(attrs={'class': 'form-control'})
        }