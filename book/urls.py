from django.urls import path
from .views import (
    book_list_view,
    book_detail_view,
    about_me,
    my_favourite_writers,
    sayings_of_great_poets,
)

urlpatterns = [
    path('', book_list_view, name='book_list'),
    path('books/<int:book_id>/', book_detail_view, name='book_detail'),
    path('about/', about_me, name='about_me'),
    path('writers/', my_favourite_writers, name='writers'),
    path('sayings/', sayings_of_great_poets, name='sayings'),
]
