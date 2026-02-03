from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter



class BookListView(generics.ListAPIView):
    """
    GET: List all books
    Permission: Read-only for anyone
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Anyone can read
     filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'title': ['exact', 'icontains'],  # exact match or partial match
        'publication_year': ['exact', 'gte', 'lte'],  # filter by year, range
        'author__name': ['exact', 'icontains'],  # filter by author's name
    }
    
    search_fields = ['title', 'author__name']

    ordering_fields = ['title', 'publication_year', 'author__name']
    ordering = ['title']

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
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Authenticated users only


class BookUpdateView(generics.UpdateAPIView):
    """
    PUT/PATCH: Update an existing book
    Permission: Only authenticated users
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


class BookDeleteView(generics.DestroyAPIView):
    """
    DELETE: Remove a book
    Permission: Only authenticated users
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookCreateView(generics.CreateAPIView):
    """
    POST: Create a new book.
    Customizations:
    - Only authenticated users can create a book.
    - Validates publication_year via serializer.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only logged-in users

    def create(self, request, *args, **kwargs):
        """
        Override create to add custom behavior
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)  # Ensures DRF validates fields
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {"message": "Book created successfully", "data": serializer.data},
            status=status.HTTP_201_CREATED,
            headers=headers
        )
class BookUpdateView(generics.UpdateAPIView):
    """
    PUT / PATCH: Update an existing book.
    Customizations:
    - Only authenticated users can update.
    - Only allow updating certain fields (optional).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)  # support PATCH
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)  # DRF validation
        self.perform_update(serializer)

        return Response(
            {"message": "Book updated successfully", "data": serializer.data},
            status=status.HTTP_200_OK
        )
