from django.db import models


class Book(models.Model):
    GENRE_CHOICES = (
        ('novel', 'Роман'),
        ('fantasy', 'Фэнтези'),
        ('detective', 'Детектив'),
        ('classic', 'Классика'),
        ('science', 'Научная литература'),
        ('poetry', 'Поэзия'),
        ('other', 'Другое'),
    )

    # 1. Название книги
    title = models.CharField(max_length=100, verbose_name="Название книги")

    # 2. Автор
    author = models.CharField(max_length=100, verbose_name="Автор")

    # 3. Описание / сюжет
    description = models.TextField(blank=True, null=True, verbose_name="Описание")

    # 4. Обложка (изображение) — нужен пакет Pillow
    image = models.ImageField(upload_to='books/', verbose_name="Обложка")

    # 5. Жанр (выбор из списка)
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES, default='other', verbose_name="Жанр")

    # 6. Количество страниц
    pages = models.PositiveIntegerField(verbose_name="Количество страниц")

    # 7. Цена
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Цена")

    # 8. Год издания
    year = models.PositiveIntegerField(blank=True, null=True, verbose_name="Год издания")

    # 9. Дата добавления (автоматически)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")

    def __str__(self):
        return f"{self.title} — {self.author}"

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
