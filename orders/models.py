from django.db import models
from django.db import models

class Order(models.Model):
    customer_name = models.CharField(max_length=100)  # Mijozning ismi
    address = models.TextField()  # Yetkazib berish manzili
    phone = models.CharField(max_length=15)  # Telefon raqami
    food_item = models.CharField(max_length=200)  # Buyurtma qilingan taom
    quantity = models.IntegerField()  # Soni
    status = models.CharField(
        max_length=20,
        choices=[('pending', 'Pending'), ('delivered', 'Delivered')],
        default='pending'
    )  # Buyurtma holati
    order_date = models.DateTimeField(auto_now_add=True)  # Buyurtma sanasi

    def __str__(self):
        return f"{self.customer_name} - {self.food_item}"
