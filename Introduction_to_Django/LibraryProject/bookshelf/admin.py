from django.contrib import admin

# Register your models here.
# include the Book model, enabling admin functionalities for it.
from .models import Book
admin.site.register(Book)
# Implement custom configurations to display title, author, and publication_year in the admin list view
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
admin.site.register(Book, BookAdmin)
# Configure list filters and search capabilities to enhance the admin’s usability for Book entries
    list_filter = ('author', 'publication_year')
    search_fields = ('title', 'author')
    