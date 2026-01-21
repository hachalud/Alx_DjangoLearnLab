<!-- Delete Data in Django -->
from bookshelf.models import Book

# Retrieve the book
book = Book.objects.get(title="1984")

# Delete the book
book.delete()