from django import forms
from .models import Book

class DateRangeForm(forms.Form):
    start_date = forms.DateField()
    end_date = forms.DateField()

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'pub_date', 'isbn', 'pages', 'language')

    widget = {
        'title': forms.TextInput(attrs={'class': 'form-control'}),
        'author': forms.TextInput(attrs={'class': 'form-control'}),
        'pub_date': forms.DateInput(attrs={'class': 'form-control'}),
        'isbn': forms.TextInput(attrs={'class': 'form-control'}),
        'pages': forms.TextInput(attrs={'class': 'form-control'}),
        'language': forms.TextInput(attrs={'class': 'form-control'}),
    }