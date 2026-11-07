import random
from datetime import timedelta

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class CustomUser(User):
    GENDER = (
        ('MALE', 'Мужской'),
        ('FEMALE', 'Женский'),
    )
    photo = models.ImageField(upload_to='users/', verbose_name="Фото")
    phone_number = models.CharField(max_length=15, verbose_name="Телефон")
    date_bir = models.DateField(verbose_name="Дата рождения")
    gender = models.CharField(max_length=10, choices=GENDER, verbose_name="Пол")
    city = models.CharField(max_length=100, verbose_name="Город")

    # Подтверждение почты (10 баллов)
    is_verified = models.BooleanField(default=False, verbose_name="Почта подтверждена")
    verification_code = models.CharField(max_length=6, blank=True, verbose_name="Код подтверждения")
    code_created_at = models.DateTimeField(null=True, blank=True)

    CODE_LIFETIME_MINUTES = 10

    def generate_code(self):
        self.verification_code = f"{random.randint(0, 999999):06d}"
        self.code_created_at = timezone.now()
        self.save(update_fields=['verification_code', 'code_created_at'])
        return self.verification_code

    def code_is_expired(self):
        if not self.code_created_at:
            return True
        return timezone.now() > self.code_created_at + timedelta(minutes=self.CODE_LIFETIME_MINUTES)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
