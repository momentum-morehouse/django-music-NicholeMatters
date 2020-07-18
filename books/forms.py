from django import forms
from .models import Book

class bookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'book_title',
            'author',
            'published_year',
            'book_cover',
            'chapter_list',
        ]
      

        # widgets = {
        # 'published_year': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        # }