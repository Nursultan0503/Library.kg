from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'product', 'quantity', 'price', 'status', 'created_at')
    list_filter = ('status', 'payment_method')
    search_fields = ('customer_name', 'product', 'phone')
    list_editable = ('status',)
