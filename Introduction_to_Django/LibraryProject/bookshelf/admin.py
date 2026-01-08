from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_year')
    list_filter = ('author', 'published_year')
    search_fields = ('title', 'author')

admin.site.register(Book, BookAdmin)
