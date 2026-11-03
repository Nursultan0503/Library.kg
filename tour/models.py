from django.contrib.auth.models import User
from django.db import models


# ---------- МНОГИЕ КО МНОГИМ ----------
# У тура много категорий, у категории много туров
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Название")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Tour(models.Model):
    title = models.CharField(max_length=150, verbose_name="Название тура")
    description = models.TextField(blank=True, verbose_name="Описание")
    image = models.ImageField(upload_to='tours/', blank=True, null=True, verbose_name="Фото")
    location = models.CharField(max_length=100, verbose_name="Место")
    duration_days = models.PositiveIntegerField(default=1, verbose_name="Длительность (дней)")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    categories = models.ManyToManyField(
        Category, related_name='tours', blank=True, verbose_name="Категории"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Тур"
        verbose_name_plural = "Туры"


# ---------- ОДИН КО МНОГИМ ----------
# У одного тура может быть много комментариев
class Comment(models.Model):
    tour = models.ForeignKey(
        Tour, on_delete=models.CASCADE, related_name='comments', verbose_name="Тур"
    )
    author = models.CharField(max_length=100, verbose_name="Имя")
    text = models.TextField(verbose_name="Комментарий")
    rating = models.PositiveSmallIntegerField(
        choices=[(i, '★' * i) for i in range(1, 6)], default=5, verbose_name="Оценка"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата")

    def __str__(self):
        return f"{self.author}: {self.tour.title}"

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ['-created_at']


# ---------- ОДИН К ОДНОМУ ----------
# Место для посещения (музей, конный тур, театр)
class Place(models.Model):
    PLACE_TYPES = (
        ('museum', 'Музей'),
        ('horse', 'Конный тур'),
        ('theatre', 'Театр'),
        ('other', 'Другое'),
    )
    name = models.CharField(max_length=150, verbose_name="Название")
    place_type = models.CharField(max_length=20, choices=PLACE_TYPES, verbose_name="Тип")
    address = models.CharField(max_length=200, blank=True, verbose_name="Адрес")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")

    def __str__(self):
        return f"{self.name} ({self.get_place_type_display()})"

    class Meta:
        verbose_name = "Место"
        verbose_name_plural = "Места"


# Человек может забронировать только ОДНО место — OneToOneField к пользователю
class Booking(models.Model):
    person = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='booking', verbose_name="Человек"
    )
    place = models.ForeignKey(
        Place, on_delete=models.CASCADE, related_name='bookings', verbose_name="Место"
    )
    visit_date = models.DateField(verbose_name="Дата посещения")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата брони")

    def __str__(self):
        return f"{self.person.username} → {self.place.name}"

    class Meta:
        verbose_name = "Бронь"
        verbose_name_plural = "Брони"
