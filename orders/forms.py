from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name', 'phone', 'product', 'product_image', 'quantity', 'price',
                  'address', 'payment_method', 'status', 'comment']
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 3}),
            'phone': forms.TextInput(attrs={'placeholder': '+996 700 123 456'}),
        }
