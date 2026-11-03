from django.urls import path
from .views import (
    order_list_view, order_detail_view, order_create_view,
    order_update_view, order_delete_view,
)

urlpatterns = [
    path('', order_list_view, name='order_list'),
    path('create/', order_create_view, name='order_create'),
    path('<int:order_id>/', order_detail_view, name='order_detail'),
    path('<int:order_id>/update/', order_update_view, name='order_update'),
    path('<int:order_id>/delete/', order_delete_view, name='order_delete'),
]
