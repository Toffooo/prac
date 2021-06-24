from rest_framework import serializers

from .models import FoodItem


class FoodModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = ("name", "calorie")
