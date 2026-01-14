from django.shortcuts import render

# Create your views here.
# Create a function-based view in relationship_app/views.py that lists all books stored in the database.
# This view should render a simple text list of book titles and their authors.
from django.http import HttpResponse
from .models import Book
def list_books(request):
    books = Book.objects.all()
    response_content = "\n".join([f"{book.title} by {book.author.name}" for book in books])
    return HttpResponse(response_content, content_type="text/plain")

# Create a class-based view in relationship_app/views.py that displays details for a specific library, listing all books available in that library.
# Utilize Django’s ListView or DetailView to structure this class-based view.
from django.views.generic import DetailView
from .models import Library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()
        return context