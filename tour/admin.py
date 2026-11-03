from django.contrib import admin
from .models import Category, Tour, Comment, Place, Booking


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'duration_days', 'price')
    list_filter = ('categories',)
    search_fields = ('title', 'location')
    filter_horizontal = ('categories',)
    inlines = [CommentInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'tour', 'rating', 'created_at')


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'place_type', 'price')
    list_filter = ('place_type',)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('person', 'place', 'visit_date')
