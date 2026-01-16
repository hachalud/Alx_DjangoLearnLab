#  include URL patterns that route to the newly created views. Make sure to link both the function-based and class-based views.
from django.urls import path
from .views import list_books, LibraryDetailView
urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    # login
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html', next_page='login'), name='logout'),
    path('register/', views.register, name='register'),
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
    path('books/add_book/', add_book, name='add_book'),
    path('books/edit_book/<int:pk>/', edit_book, name='edit_book'),
    path('books/delete_book/<int:pk>/', delete_book, name='delete_book'),
]