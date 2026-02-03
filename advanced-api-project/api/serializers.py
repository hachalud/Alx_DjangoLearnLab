from rest_framework import serializers
from datetime import date
from .models import Author, Book
class BookSerializer(serializers.ModelSerializer):
    """
    BookSerializer:
    ----------------
    This serializer is responsible for converting Book model instances
    into JSON format and validating incoming book data.

    It includes custom validation to ensure that the publication year
    is not set in the future.
    """

    class Meta:
        model = Book
        fields = "__all__"  # Serialize all fields of the Book model

    def validate_publication_year(self, value):
        """
        Custom validation method to ensure the publication year
        is not greater than the current year.
        """
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future."
            )
        return value

class AuthorSerializer(serializers.ModelSerializer):
    """
    AuthorSerializer:
    ------------------
    This serializer handles the serialization of Author model data.

    It includes a nested BookSerializer to dynamically serialize
    all books related to a specific author.
    """

    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ["id", "name", "books"]
