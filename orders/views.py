from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .forms import OrderForm
from .models import Order


# READ — список заказов (поиск + фильтр по статусу)
def order_list_view(request):
    orders = Order.objects.all()
    query = request.GET.get('q', '')
    status = request.GET.get('status', '')
    if query:
        orders = orders.filter(Q(customer_name__icontains=query) | Q(product__icontains=query))
    if status:
        orders = orders.filter(status=status)
    return render(request, 'orders/order_list.html', {
        'orders': orders,
        'statuses': Order.STATUS_CHOICES,
        'query': query,
        'current_status': status,
    })


# READ — один заказ
def order_detail_view(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'orders/order_detail.html', {'order': order})


# CREATE — новый заказ
def order_create_view(request):
    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            order = form.save()
            return redirect('order_detail', order_id=order.id)
    else:
        form = OrderForm()
    return render(request, 'orders/order_form.html', {'form': form, 'title': 'Новый заказ'})


# UPDATE — редактирование заказа
def order_update_view(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_detail', order_id=order.id)
    else:
        form = OrderForm(instance=order)
    return render(request, 'orders/order_form.html', {
        'form': form, 'title': f'Редактирование заказа №{order.id}', 'order': order,
    })


# DELETE — удаление заказа (с подтверждением)
def order_delete_view(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        order.delete()
        return redirect('order_list')
    return render(request, 'orders/order_confirm_delete.html', {'order': order})
