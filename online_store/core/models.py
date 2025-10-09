
from django.db import models


class Users(models.Model):
    # Добавим поле Role с choices
    ROLE_CHOICES = [
        ('Buyer', 'Покупатель'),
        ('Seller', 'Продавец')
    ]

    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField(unique=True, verbose_name='Email')
    password = models.CharField(max_length=100, verbose_name='Пароль')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Buyer',
                            verbose_name='Роль')  # Исправил на строчную букву
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.name


class Categories(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название категории')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name