<!-- retrieve book -->
from bookshelf.models import Book

# Retrieve the book
book = Book.objects.get(title="1984")

# Display all attributes
for field in book._meta.fields:
    print(f"{field.name}: {getattr(book, field.name)}")