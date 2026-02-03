from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
# Create your views here.
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [TokenAuthentication] 
    def get_permissions(self):
        """
        Assign permissions based on action
        """
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticated]  # Any authenticated user
        else:
            permission_classes = [IsAdminUser]      # Only admins for create/update/delete
        return [permission() for permission in permission_classes] # Require token
    permission_classes = [IsAuthenticated]
from rest_framework.permissions import BasePermission

class IsLibrarian(BasePermission):
    """
    Only users with `is_staff=True` can perform write actions
    """
    def has_permission(self, request, view):
        if view.action in ['list', 'retrieve']:
            return request.user and request.user.is_authenticated
        return request.user and request.user.is_staff
permission_classes = [IsLibrarian]