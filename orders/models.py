from django.db import models


class Order(models.Model):
    STATUS_CHOICES = (
        ('new', 'Новый'),
        ('paid', 'Оплачен'),
        ('shipped', 'Отправлен'),
        ('delivered', 'Доставлен'),
        ('cancelled', 'Отменён'),
    )
    PAYMENT_CHOICES = (
        ('card', 'Картой'),
        ('cash', 'Наличными'),
        ('elqr', 'ЭЛКАРТ / QR'),
    )

    customer_name = models.CharField(max_length=100, verbose_name="Покупатель")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    product = models.CharField(max_length=200, verbose_name="Товар")
    product_image = models.ImageField(upload_to='orders/', blank=True, null=True, verbose_name="Фото товара")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Количество")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена за шт.")
    address = models.CharField(max_length=255, verbose_name="Адрес доставки")
    payment_method = models.CharField(max_length=10, choices=PAYMENT_CHOICES, default='card', verbose_name="Оплата")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new', verbose_name="Статус")
    comment = models.TextField(blank=True, verbose_name="Комментарий")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Изменён")

    @property
    def total(self):
        return self.quantity * self.price

    def __str__(self):
        return f"Заказ №{self.id} — {self.product}"

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        ordering = ['-created_at']
