from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.db import models
from users.managers import CustomUserManager


class CustomUser(AbstractUser):
    """Кастомная модель для пользователей"""
    username = None
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    phone_number = models.CharField(
        max_length=25,
        validators=[MinLengthValidator(6)],
        unique=True
    )
    objects = CustomUserManager()

    class Meta:
        verbose_name_plural = 'Пользователи'
        verbose_name = 'Пользователь'