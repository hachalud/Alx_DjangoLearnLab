from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters import rest_framework as filters

# Fix for using your intended syntax
filters.SearchFilter = SearchFilter
filters.OrderingFilter = OrderingFilter

# List all books with filtering, search, and ordering
class BookListView(generics.ListAPIView):
    """
    GET: List all books
    Permission: Read-only for anyone
    Features: filtering, search, ordering
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

    # Correct indentation and proper use of filters
    filter_backends = [
        filters.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]

    filterset_fields = {
        'title': ['exact', 'icontains'],
        'publication_year': ['exact', 'gte', 'lte'],
        'author__name': ['exact', 'icontains'],
    }

    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year', 'author__name']
    ordering = ['title']


# Retrieve a single book
class BookDetailView(generics.RetrieveAPIView):
    """
    GET: Retrieve a single book by ID
    Permission: Read-only for anyone
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# Create a new book
class BookCreateView(generics.CreateAPIView):
    """
    POST: Create a new book
    Permission: Only authenticated users
    Customizes response message
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {"message": "Book created successfully", "data": serializer.data},
            status=status.HTTP_201_CREATED,
            headers=headers
        )


# Update an existing book
class BookUpdateView(generics.UpdateAPIView):
    """
    PUT/PATCH: Update an existing book
    Permission: Only authenticated users
    Customizes response message
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(
            {"message": "Book updated successfully", "data": serializer.data},
            status=status.HTTP_200_OK
        )


# Delete a book
class BookDeleteView(generics.DestroyAPIView):
    """
    DELETE: Remove a book
    Permission: Only authenticated users
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
