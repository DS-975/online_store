from django.db import models
from core.models import Users
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class SellerProfile(models.Model):
    user_id = models.OneToOneField(Users, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    description = models.TextField()
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)]) # Валидаторы помогаю установить минимально и максимально допустимое значение
    total_sales = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Профиль продавца"
        verbose_name_plural = "Профили продавцов"
