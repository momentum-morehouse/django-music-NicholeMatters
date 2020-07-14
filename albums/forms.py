from django import forms
from .models import Album

class albumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = [
            'title',
            'artist',
            'released',
            
        ]
        # widgets = {'birthday': forms.SelectDateWidget()
        # }
