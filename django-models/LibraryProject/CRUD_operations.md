<!-- CRUD Operations in Django -->
<!-- Create Data in Django -->
from bookshelf.models import Book
book = Book(title="1984", author="George Orwell", publication_year="1949")
book.save()
book

<!-- Retrieve Data in Django -->
from bookshelf.models import Book

# Retrieve the book
book = Book.objects.get(title="1984")

# Display all attributes
for field in book._meta.fields:
    print(f"{field.name}: {getattr(book, field.name)}")

<!-- Update Data in Django -->
from bookshelf.models import Book

# Retrieve the book
book = Book.objects.get(title="1984")

# Update the book
book.title = "Nineteen Eighty-Four"
book.save()

<!-- Delete Data in Django -->
from bookshelf.models import Book

# Retrieve the book
book = Book.objects.get(title="1984")

# Delete the book
book.delete()