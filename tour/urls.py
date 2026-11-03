from django.urls import path
from .views import tour_list_view, tour_detail_view, booking_list_view

urlpatterns = [
    path('', tour_list_view, name='tour_list'),
    path('<int:tour_id>/', tour_detail_view, name='tour_detail'),
    path('bookings/', booking_list_view, name='booking_list'),
]
