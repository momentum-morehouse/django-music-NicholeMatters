from django import forms
from .models import Album, Details

class albumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = [
            'title',
            'artist',
            'released',
            'image_url',
            
        ]
        widgets = {'released': forms.SelectDateWidget()
        }

class DetailForm(forms.ModelForm):
  class Meta:
    model = Details
    fields = ['text']