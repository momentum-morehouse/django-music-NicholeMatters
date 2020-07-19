from django import forms
from .models import Album, Book

class albumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = [
            'title',
            'artist',
            'released',
            'image_url',
            'track_list',
        ]
      

        widgets = {
        'date_released': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        }

        

class bookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'book_title',
            'author',
            'date_published',
            'book_cover',
            'chapter_list',
        ]
      

        widgets = {
        'date_published': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        }