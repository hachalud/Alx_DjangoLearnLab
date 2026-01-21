from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    """
    Secure form for creating and editing Book objects.
    Django forms automatically validate and sanitize user input.
    """

    class Meta:
        model = Book
        fields = ["title", "author", "published_date"]
