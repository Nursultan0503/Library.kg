from django.urls import path
from .views import about_me, my_favourite_writers, sayings_of_great_poets

urlpatterns = [
    path('about/', about_me, name='about_me'),
    path('writers/', my_favourite_writers, name='writers'),
    path('sayings/', sayings_of_great_poets, name='sayings'),
]