from django.db import models


class FoodItem(models.Model):
    name = models.CharField(max_length=255)
    calorie = models.FloatField()
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)
