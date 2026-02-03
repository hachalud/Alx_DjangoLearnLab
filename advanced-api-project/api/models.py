from django.db import models

# ------------------------------
# Author model
# ------------------------------
class Author(models.Model):
    """
    Author Model:
    -------------
    Represents an author who can write multiple books.

    Fields:
    - name: stores the author's name.
    Relationship:
    - One Author can have many Books (one-to-many).
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# ------------------------------
# Book model
# ------------------------------
class Book(models.Model):
    """
    Book Model:
    -----------
    Represents a book written by an author.

    Fields:
    - title: title of the book
    - publication_year: the year the book was published (integer)
    - author: foreign key linking to Author
    Relationship:
    - Each book belongs to one Author
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(
        Author,
        related_name='books',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title