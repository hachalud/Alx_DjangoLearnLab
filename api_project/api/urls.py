from django.urls import path
from rest_framework import routers
from api import views
from .views import BookList, BookViewSet
from django.urls import include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
router = DefaultRouter()
router.register(r'books', views.BookViewSet, basename='book_all')
urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),
    path('', include(router.urls)),
]
