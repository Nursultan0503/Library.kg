from django.shortcuts import render, get_object_or_404
from .models import Tour, Category, Booking


# Список туров (+ фильтр по категории: многие ко многим)
def tour_list_view(request):
    tours = Tour.objects.prefetch_related('categories').order_by('-created_at')
    categories = Category.objects.all()
    category_id = request.GET.get('category')
    if category_id:
        tours = tours.filter(categories__id=category_id)
    return render(request, 'tour/tour_list.html', {
        'tours': tours,
        'categories': categories,
        'current_category': category_id,
    })


# Детальная страница тура: категории + комментарии (один ко многим)
def tour_detail_view(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    comments = tour.comments.all()
    return render(request, 'tour/tour_detail.html', {'tour': tour, 'comments': comments})


# Список броней (один к одному: один человек — одна бронь)
def booking_list_view(request):
    bookings = Booking.objects.select_related('person', 'place')
    return render(request, 'tour/booking_list.html', {'bookings': bookings})
