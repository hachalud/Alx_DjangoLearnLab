from django.urls import path
from rest_framework import routers
from api import views
from .views import BookList, BookViewSet
from django.urls import include
from rest_framework import defaultsRouter
router = defaultsRouter()
router.register(r'books', views.BookViewSet, basename='book_all')
router = routers.DefaultRouter()
router.register(r'books', views.BookViewSet)
urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('api/', include('api.urls')),
    path('', include(router.urls)),
]
