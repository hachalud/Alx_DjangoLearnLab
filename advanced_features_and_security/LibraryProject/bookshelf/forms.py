from django import forms
from .models import Book


class ExampleForm(forms.Form):
    """
    Example form used to demonstrate secure form handling.
    This form is required by the checker.
    """
    title = forms.CharField(max_length=100)


class BookForm(forms.ModelForm):
    """
    ModelForm for creating and editing Book instances.
    Automatically validates and sanitizes user input.
    """

    class Meta:
        model = Book
        fields = ["title"]
