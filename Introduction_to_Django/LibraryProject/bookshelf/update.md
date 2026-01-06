<!-- Update Data in Django -->
from bookshelf.models import Book

# Retrieve the book
book = Book.objects.get(title="1984")

# Update the book
book.title = "Nineteen Eighty-Four"
book.save()