from django.urls import path
from .views import create_book_form


urlpatterns = [
    path('htmx/create-book-form/', create_book_form, name='create-book-form'),
]
